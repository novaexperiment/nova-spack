# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftNdReco(NovasoftPackage):
    """NOvA near-detector reconstruction summary objects and art module."""

    root_cmakelists_dir = "NDReco"

    depends_on("art")
    depends_on("art-root-io")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("fhicl-cpp")
    depends_on("messagefacility")
    depends_on("novasoft-calibrator")
    depends_on("novasoft-cvn")
    depends_on("novasoft-geometry")
    depends_on("novasoft-live-geometry")
    depends_on("novasoft-geometry-objects")
    depends_on("novasoft-mccheater")
    depends_on("novasoft-re-mid")
    depends_on("novasoft-reco-base")
    depends_on("novasoft-reco-base-hit")
    depends_on("novasoft-simulation")
    depends_on("novasoft-summary-data")
    depends_on("novasoft-timing-fit")
    depends_on("novasoft-utilities")
    depends_on("nusimdata")
    depends_on("root")
