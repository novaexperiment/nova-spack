# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Novadaq(CMakePackage):
    """NOvA DAQ package"""

    homepage = "https://www.github.com/novaexperiment/novasoft"
    git = "git@github.com:novaexperiment/novadaq"

    root_cmakelists_dir = "pkgs"

    maintainers("vhewes")

    version("develop", branch="main")

    variant(
        "cxxstd",
        default="17",
        values=("17", "20", "23"),
        multi=False,
        sticky=True,
        description="C++ standard",
    )

    depends_on("cetmodules", type="build")

    depends_on("boost")
    depends_on("libwda")
    depends_on("messagefacility")
    depends_on("postgresql")
    depends_on("xerces-c")
    depends_on("xsd")
