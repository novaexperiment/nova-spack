from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftCafMaker(NovasoftPackage):
    """NOvA CAF-making art producer and support library."""

    root_cmakelists_dir = "CAFMaker"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "eigen",
        "fhicl-cpp",
        "ifdhc",
        "messagefacility",
        "novasoft-beamline-reco-base",
        "novasoft-beamline-sim-base",
        "novasoft-break-point-fitter",
        "novasoft-cos-rej",
        "novasoft-cvn",
        "novasoft-lem",
        "novasoft-mccheater",
        "novasoft-mc-reweight",
        "novasoft-me-finder",
        "novasoft-metadata",
        "novasoft-muon-id",
        "novasoft-ncid",
        "novasoft-nd-reco",
        "novasoft-numu-energy",
        "novasoft-numu-sandbox",
        "novasoft-nus-sandbox",
        "novasoft-preselection",
        "novasoft-qe-event-finder",
        "novasoft-raw-data",
        "novasoft-re-mid",
        "novasoft-reco-base",
        "novasoft-reco-jm-shower",
        "novasoft-rec-var-pid",
        "novasoft-shower-lid",
        "novasoft-simulation",
        "novasoft-standard-record",
        "novasoft-summary-data",
        "novasoft-tensorflow-products",
        "novasoft-test-beam-utils",
        "novasoft-track-info",
        "novasoft-xnue-pid",
        "novasoft-xsec-reco",
        "nusimdata",
        "osclib",
        "root",
    ):
        depends_on(dep)
