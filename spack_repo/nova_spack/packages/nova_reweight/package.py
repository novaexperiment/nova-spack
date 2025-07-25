# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class NovaReweight(CMakePackage):
    """NOvA cross-section reweighting toolkit"""

    homepage = "https://www.github.com/novaexperiment/novarwgt"
    git = "git@github.com:novaexperiment/novarwgt"

    maintainers("vhewes")

    version("3.0.12", tag="v3.0-dev12")
    version("3.0.6", tag="v3.0-dev6")

    variant(
        "cxxstd",
        default="17",
        values=("17", "20", "23"),
        multi=False,
        sticky=True,
        description="C++ standard",
    )

    depends_on("root")

    depends_on("cetbuildtools", type="build")
    depends_on("cetmodules", type="build")

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

    def cmake_args(self):
        return [
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            self.define_from_variant("NOVARWGT_USE_CETLIB", "cetlib"),
            self.define_from_variant("NOVARWGT_USE_GENIE", "genie"),
            self.define_from_variant("NOVARWGT_USE_NUSIMDATA", "nusimdata"),
        ]

    def setup_build_environment(self, env):
        if self.spec.satisfies("+genie"):
            env.set("PYTHIA6_LIBRARY", self.spec["pythia6"].prefix.lib)
            env.set("GENIE_REWEIGHT", self.spec["genie"].prefix)
        if self.spec.satisfies("+nusimdata"):
            nusimdata_version = "v{}".format(self.spec["nusimdata"].version.underscored)
            env.set("NUSIMDATA_VERSION", nusimdata_version)
            env.set("NUSIMDATA_INC", self.spec["nusimdata"].prefix.include)
            env.set("NUSIMDATA_LIB", self.spec["nusimdata"].prefix.lib)

    @run_after("install")
    def alias_include_paths(self):
        mkdirp(prefix.inc.StandardRecord) 
        symlink("../NOvARwgt", prefix.inc.StandardRecord.NOvARwgt)
