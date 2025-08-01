# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Osclib(CMakePackage):
    """Neutrino oscillation probability tools."""

    homepage = "https://github.com/cafana/OscLib"
    url = "https://github.com/cafana/OscLib/archive/v01.00.tar.gz"
    git = "https://github.com/cafana/OscLib"

    maintainers("vhewes")

    version("main", branch="main")
    version("01.00", sha256="0e46970f017890727c4c1f38dafc7bc2603cb45a050e3c59732b12768b32d4a4")

    depends_on("cetmodules", type="build")

    depends_on("root")
    depends_on("boost")
    depends_on("eigen")

    with when("+stan"):
        depends_on("stan-math")
        depends_on("sundials")
        depends_on("tbb")

    # patch cmake build for v1.0
    patch("https://github.com/cafana/OscLib/commit/b0aa742ecd8c5604c4ca61a2e9b2015524401f70.patch",
          sha256="fbd46220e9df966ba355aec4ea565d0a1541e2e26debe3a5206c77a36ed4875d", when="@01.00")
    
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
            env.set("STAN_MATH_INC", self.spec["stan-math"].prefix.include)

    def cmake_args(self):
        return [
            self.define_from_variant("STAN", "stan"),
            self.define("TBB_ONEAPI", "intel-tbb-oneapi" in self.spec),
        ]
