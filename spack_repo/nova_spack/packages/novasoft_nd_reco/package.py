from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftNdReco(NovasoftPackage):
    """NOvA near-detector reconstruction summary objects and art module."""

    root_cmakelists_dir = "NDReco"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "novasoft-calibrator",
        "novasoft-cvn",
        "novasoft-geometry",
        "novasoft-live-geometry",
        "novasoft-geometry-objects",
        "novasoft-mccheater",
        "novasoft-re-mid",
        "novasoft-reco-base",
        "novasoft-reco-base-hit",
        "novasoft-simulation",
        "novasoft-summary-data",
        "novasoft-timing-fit",
        "novasoft-utilities",
        "nusimdata",
        "root",
    ):
        depends_on(dep)
