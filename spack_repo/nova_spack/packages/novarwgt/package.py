# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Novarwgt(CMakePackage):
    """NOvA cross-section reweighting toolkit"""

    homepage = "https://www.github.com/novaexperiment/novarwgt"
    git = "git@github.com:novaexperiment/novarwgt"

    maintainers("vhewes")

    version("4.0.4", tag="v4.0-dev4",
            commit="ac515a3175a02b42eac5892b20f158710d3bb55d")
    version("3.0.16", tag="v3.0-dev16")

    variant(
        "cxxstd",
        default="17",
        values=("17", "20", "23"),
        multi=False,
        sticky=True,
        description="C++ standard",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cetbuildtools", type="build")
    depends_on("cetmodules", type="build")

    depends_on("nufinder")
    depends_on("root")

    patch("cmake-3.0.16.patch", when="@3.0.16",
          sha256="26fcb6c9718034a494a536a79ff5b2d64243105a3a2ad7e947dc61c94ef29d0a")

    def patch(self):
        filter_file("/src", "/include/GENIE", "cmake/Modules/FindGENIE.cmake")

    # optional cetlib dependency
    variant("cetlib", default=False, description="Enable CETLib dependency")
    depends_on("cetlib", when="+cetlib")

    # optional genie dependency
    variant("genie", default=True, description="Enable GENIE dependency")
    depends_on("nufinder", when="+genie")
    depends_on("genie", when="+genie")

    # optional nusimdata dependency
    variant("nusimdata", default=True, description="Enable NuSimData dependency")
    depends_on("nusimdata", when="+nusimdata")

    variant("nusystematics", default=True, when="@4:",
            description="Enable nusystematics dependency")
    depends_on("nusystematics", when="+nusystematics")
    depends_on("nuhepmc-cmake-modules", type="build", when="+nusystematics")

    def cmake_args(self):
        args = [
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            self.define_from_variant("NOVARWGT_USE_CETLIB", "cetlib"),
            self.define_from_variant("NOVARWGT_USE_GENIE", "genie"),
            self.define_from_variant("NOVARWGT_USE_NUSIMDATA", "nusimdata"),
            self.define_from_variant("NOVARWGT_USE_NUSYSTEMATICS", "nusystematics"),
        ]
        if self.spec.satisfies("+nusystematics"):
            args += [self.define("CMAKE_MODULE_PATH", self.spec['nuhepmc-cmake-modules'].prefix.cmake)]
        return args

    def setup_build_environment(self, env):
        if self.spec.satisfies("+genie"):
            env.set("PYTHIA6_LIBRARY", self.spec["pythia6"].prefix.lib)
            env.set("GENIE_REWEIGHT", self.spec["genie"].prefix)
            env.set("LOG4CPP_INC", self.spec["log4cpp"].prefix.include)
            env.set("LOG4CPP_LIB", self.spec["log4cpp"].prefix.lib)
        if self.spec.satisfies("+nusimdata"):
            nusimdata_version = "v{}".format(self.spec["nusimdata"].version.underscored)
            env.set("NUSIMDATA_VERSION", nusimdata_version)
            env.set("NUSIMDATA_INC", self.spec["nusimdata"].prefix.include)
            env.set("NUSIMDATA_LIB", self.spec["nusimdata"].prefix.lib)

    @run_after("install")
    def alias_include_paths(self):
        mkdirp(prefix.inc.StandardRecord) 
        symlink("../NOvARwgt", prefix.inc.StandardRecord.NOvARwgt)
