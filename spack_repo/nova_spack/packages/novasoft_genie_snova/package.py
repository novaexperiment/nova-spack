# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftGenieSnova(NovasoftPackage):
    """NOvA supernova GENIE flux generation tools."""

    root_cmakelists_dir = "GenieSNova"

    depends_on("boost")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("fhicl-cpp")
    depends_on("genie")
    depends_on("gsl")
    depends_on("lhapdf")
    depends_on("libxml2")
    depends_on("log4cpp")
    depends_on("messagefacility")
    depends_on("nusimdata")
    depends_on("pythia6")
    depends_on("root")
