# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftAnalysisSkimmer(NovasoftPackage):
    """NOvA configurable analysis skimming libraries and art modules."""

    root_cmakelists_dir = "AnalysisSkimmer"

    depends_on("art")
    depends_on("art-root-io")
    depends_on("boost")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("fhicl-cpp")
    depends_on("messagefacility")
    depends_on("novasoft-cos-rej")
    depends_on("novasoft-cvn")
    depends_on("novasoft-geometry")
    depends_on("novasoft-lem")
    depends_on("novasoft-live-geometry")
    depends_on("novasoft-mccheater")
    depends_on("novasoft-mc-reweight")
    depends_on("novasoft-me-finder")
    depends_on("novasoft-numu-energy")
    depends_on("novasoft-numu-sandbox")
    depends_on("novasoft-preselection")
    depends_on("novasoft-qe-event-finder")
    depends_on("novasoft-re-mid")
    depends_on("novasoft-reco-base")
    depends_on("novasoft-summary-data")
    depends_on("novasoft-utilities")
    depends_on("nusimdata")
    depends_on("root")
