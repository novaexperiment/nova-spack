from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftMcCheckOut(NovasoftPackage):
    """NOvA Monte Carlo validation and checkout modules."""

    root_cmakelists_dir = "MCCheckOut"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "novasoft-cmap",
        "novasoft-geometry",
        "novasoft-geometry-objects",
        "novasoft-mccheater",
        "novasoft-mc-reweight",
        "novasoft-raw-data",
        "novasoft-reco-base",
        "novasoft-reco-base-hit",
        "novasoft-simulation",
        "novasoft-standard-record",
        "novasoft-summary-data",
        "nusimdata",
        "root",
    ):
        depends_on(dep)
