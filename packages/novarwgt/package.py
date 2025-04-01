# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Novarwgt(CMakePackage):
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

    depends_on("cetmodules", type="build")

    patch("patch/v3-0-12.patch", when="@3.0.12")
    patch("patch/v3-0-6.p", when="@3.0.6")

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
