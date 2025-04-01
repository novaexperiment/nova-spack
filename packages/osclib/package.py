# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Osclib(CMakePackage):
    """Neutrino oscillation probability tools."""

    homepage = "https://github.com/cafana/OscLib"
    url = "https://github.com/cafana/OscLib/archive/v00.25.tar.gz"
    git = "https://github.com/cafana/OscLib"

    maintainers("vhewes")

    version("main", branch="main")
    version("00.26", sha256="e5eb84641428d4dcb59e3ac1f082d3d9dc18a13ee598aee9def82c0b1861de42")
    version("00.25", sha256="ee4f4120e414acb065ad967bda9de12e7a5594e6539b25b721084c8f112a3f4c")

    depends_on("cetmodules", type="build")

    depends_on("root")
    depends_on("boost")
    depends_on("eigen")

    with when("+stan"):
        depends_on("stan-math")
        depends_on("tbb")

    patch("tbb.patch", when="@:00.26")
    
    def patch(self):
        # fix numeric version string in CMakeLists.txt
        if not self.version.isdevelop():
            filter_file(r"project\(osclib VERSION .+?\)",
                        f"project(osclib VERSION {self.version})",
                        "CMakeLists.txt")

    variant("stan", default=True, description="Build with Stan dependency")

    def setup_build_environment(self, env):
        # need to set up STAN_MATH_INC so Findstan_math.cmake will work as-is
        if self.spec.satisfies("+stan"):
            env.set("STAN_MATH_INC", self.spec["stan-math"].prefix)

    def cmake_args(self):
        return [
            self.define_from_variant("STAN", "stan"),
            self.define("TBB_ONEAPI", "intel-tbb-oneapi" in self.spec),
        ]
