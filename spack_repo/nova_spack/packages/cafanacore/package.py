# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Cafanacore(CMakePackage):
    """Base libraries of the CAFAna analysis framework"""

    homepage = "https://github.com/cafana/CAFAnaCore"
    url = "https://github.com/cafana/CAFAnaCore/archive/v02.01.tar.gz"

    maintainers("vhewes")

    version("02.01", sha256="cb747ef71586bead03233ef58ad038c8e133b7c210971e8e6ba6df0cbef7e1ae")
    version("01.40", sha256="7eafc0f0b7362c30b9d0017286bf1d4548b8fe20f70ab9809242582923fe424f")

    variant("stan", default=True, description="Build with Stan Math support")
    variant("ifdhc", default=True, description="Build with IFDHC support")
    variant("cxxstd", values=("17", "20", "23"), default="17", multi=False,
            sticky=True, description="C++ standard")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cetmodules", type="build")

    depends_on("boost")
    depends_on("osclib")
    with when("+stan"):
        depends_on("osclib+stan")
        depends_on("stan-math")
        depends_on("sundials")
    depends_on("ifdhc", when="+ifdhc")

    # link against SUNDIALS target
    patch("https://github.com/cafana/CAFAnaCore/commit/c00681908935d440028a3f33a1b9c16440ec4a7e.patch",
          sha256="86a88211ddcb84dc09110435d6eb8b2305c676d2b2b50b01cf52414f58cc7db4", when="@01.40")

    def setup_build_environment(self, env):

        # stan-math
        env.set("STAN_MATH_DIR", self.spec["stan-math"].prefix)
        env.set("STAN_MATH_VERSION", self.spec["stan-math"].version)
        env.set("STAN_MATH_INC", self.spec["stan-math"].prefix.include)

        # sundials
        env.set("SUNDIALS_INC", self.spec["sundials"].prefix.include)

        # ifdhc
        if self.spec.satisfies("+ifdhc"):
            env.set("IFDHC_DIR", self.spec["ifdhc"].prefix)
            env.set("IFDHC_FQ_DIR", self.spec["ifdhc"].prefix)
            env.set("IFDHC_VERSION", self.spec["ifdhc"].version)
            env.set("IFDHC_INC", self.spec["ifdhc"].prefix.inc)
            env.set("IFDHC_LIB", self.spec["ifdhc"].prefix.lib)

    def cmake_args(self):
        return [
            self.define("SPACK", "YES"),
            self.define("CAFANACORE_VERSION", self.spec.version),
            self.define("NO_IFDHC", self.spec.satisfies("~ifdhc")),
            self.define_from_variant("STAN", "stan"),
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
        ]

    @run_after("install")
    def alias_include_paths(self):
        mkdir(prefix.inc.CAFAnaCore) 
        symlink("../CAFAna", prefix.inc.CAFAnaCore.CAFAna)
