from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftAnalysisSkimmer(NovasoftPackage):
    """NOvA configurable analysis skimming libraries and art modules."""

    root_cmakelists_dir = "AnalysisSkimmer"

    for dep in (
        "art",
        "art-root-io",
        "boost",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "novasoft-cos-rej",
        "novasoft-cvn",
        "novasoft-geometry",
        "novasoft-lem",
        "novasoft-live-geometry",
        "novasoft-mccheater",
        "novasoft-mc-reweight",
        "novasoft-me-finder",
        "novasoft-numu-energy",
        "novasoft-numu-sandbox",
        "novasoft-preselection",
        "novasoft-qe-event-finder",
        "novasoft-re-mid",
        "novasoft-reco-base",
        "novasoft-summary-data",
        "novasoft-utilities",
        "nusimdata",
        "root",
    ):
        depends_on(dep)
