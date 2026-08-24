from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftFastMonopole(NovasoftPackage):
    """Fast monopole reconstruction and analysis modules."""

    root_cmakelists_dir = "FastMonopole"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "nova-daq",
        "novasoft-calibrator",
        "novasoft-cmap",
        "novasoft-geometry",
        "novasoft-geometry-objects",
        "novasoft-mccheater",
        "novasoft-raw-data",
        "novasoft-reco-base",
        "novasoft-simulation",
        "novasoft-utilities",
        "nusimdata",
        "root",
    ):
        depends_on(dep)
