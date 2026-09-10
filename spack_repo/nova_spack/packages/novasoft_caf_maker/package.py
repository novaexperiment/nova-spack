# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftCafMaker(NovasoftPackage):
    """NOvA CAF-making art producer and support library."""

    root_cmakelists_dir = "CAFMaker"

    depends_on("art")
    depends_on("art-root-io")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("eigen")
    depends_on("fhicl-cpp")
    depends_on("ifdh-art")
    depends_on("ifdhc")
    depends_on("messagefacility")
    depends_on("nova-daq")
    depends_on("novasoft-beamline-reco-base")
    depends_on("novasoft-beamline-sim-base")
    depends_on("novasoft-break-point-fitter")
    depends_on("novasoft-cos-rej")
    depends_on("novasoft-cvn")
    depends_on("novasoft-lem")
    depends_on("novasoft-mccheater")
    depends_on("novasoft-mc-reweight")
    depends_on("novasoft-me-finder")
    depends_on("novasoft-metadata")
    depends_on("novasoft-muon-id")
    depends_on("novasoft-ncid")
    depends_on("novasoft-nd-reco")
    depends_on("novasoft-numu-energy")
    depends_on("novasoft-numu-sandbox")
    depends_on("novasoft-nus-sandbox")
    depends_on("novasoft-preselection")
    depends_on("novasoft-qe-event-finder")
    depends_on("novasoft-raw-data")
    depends_on("novasoft-re-mid")
    depends_on("novasoft-reco-base")
    depends_on("novasoft-reco-jm-shower")
    depends_on("novasoft-rec-var-pid")
    depends_on("novasoft-shower-lid")
    depends_on("novasoft-simulation")
    depends_on("novasoft-standard-record")
    depends_on("novasoft-summary-data")
    depends_on("novasoft-tensorflow-products")
    depends_on("novasoft-test-beam-utils")
    depends_on("novasoft-track-info")
    depends_on("novasoft-xnue-pid")
    depends_on("novasoft-xsec-reco")
    depends_on("nusimdata")
    depends_on("osclib")
    depends_on("root")
