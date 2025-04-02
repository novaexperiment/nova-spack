# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Cafanacore(CMakePackage):
    """Base libraries of the CAFAna analysis framework"""

    homepage = "https://github.com/cafana/CAFAnaCore"
    url = "https://github.com/cafana/CAFAnaCore/archive/v02.01.tar.gz"

    maintainers("vhewes")

    version("02.01", sha256="cb747ef71586bead03233ef58ad038c8e133b7c210971e8e6ba6df0cbef7e1ae")
    version("01.36", sha256="f8441698fa89aab33da6a9044c267138ef56e58d06023b7027a6632738e81841")

    variant("stan", default=True, description="Build with Stan Math support")
    variant("ifdhc", default=True, description="Build with IFDHC support")
    variant("cxxstd", values=("17", "20", "23"), default="17", multi=False,
            sticky=True, description="C++ standard")

    depends_on("cetmodules", type="build")
    depends_on("boost")
    depends_on("osclib")
    depends_on("osclib+stan", when="+stan")
    depends_on("stan-math")
    depends_on("ifdhc", when="+ifdhc")

    # add std::optional include
    patch("https://github.com/cafana/CAFAnaCore/commit/6dbb3ca66d3baed477c5659b3403f7d1a2f88ef4.patch",
          sha256="5f034e885b92d3f8000d4156c2b0e08d78b53e362194b21c1952acc8bf013030", when="@:1")

    # update CMake build for spack
    patch("https://github.com/cafana/CAFAnaCore/commit/fe2f843d73d7acfb6ba4a9c90e3c068c734ee5c1.patch",
          sha256="2bbecfd1b7bdce5450afcb294d0ee826e3c45fef7fb8fe7b3bd6c7192422776a", when="@:1")

    def setup_build_environment(self, env):

        # stan-math
        env.set("STAN_MATH_DIR", self.spec["stan-math"].prefix)
        env.set("STAN_MATH_VERSION", self.spec["stan-math"].version)
        env.set("STAN_MATH_INC", self.spec["stan-math"].prefix)

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
