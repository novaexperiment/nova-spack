from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftCellHitTimeAna(NovasoftPackage):
    """NOvA cell-hit timing analysis module."""

    root_cmakelists_dir = "CellHitTimeAna"

    for dep in (
        "art",
        "art-root-io",
        "cafanacore",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "novasoft-3-flavor-ana",
        "novasoft-calibrator",
        "novasoft-geometry",
        "novasoft-geometry-objects",
        "novasoft-numu-energy-func",
        "novasoft-re-mid",
        "novasoft-reco-base",
        "novasoft-slicer",
        "novasoft-standard-record",
        "novasoft-utilities-func",
        "root",
    ):
        depends_on(dep)
