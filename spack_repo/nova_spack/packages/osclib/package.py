# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Osclib(CMakePackage):
    """Neutrino oscillation probability tools."""

    homepage = "https://github.com/cafana/OscLib"
    url = "https://github.com/cafana/OscLib/archive/v1.0.1.tar.gz"
    git = "https://github.com/cafana/OscLib"

    maintainers("vhewes")

    version("main", branch="main")
    version("1.0.1", sha256="9a5456e884dc706849dfbfc7dda26f37cab58bc965eec80d4a02b9c5b9a0ec4d")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cetmodules", type="build")

    depends_on("root")
    depends_on("boost")
    depends_on("eigen")

    with when("+stan"):
        depends_on("stan-math")
        depends_on("sundials")
        depends_on("tbb")

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
