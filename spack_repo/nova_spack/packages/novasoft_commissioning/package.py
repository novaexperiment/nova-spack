from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftCommissioning(NovasoftPackage):
    """NOvA detector commissioning modules."""

    root_cmakelists_dir = "Commissioning"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "nova-daq",
        "novasoft-cmap",
        "novasoft-geometry",
        "novasoft-geometry-objects",
        "novasoft-raw-data",
        "novasoft-reco-base",
        "novasoft-summary-data",
        "novasoft-track-fit",
        "novasoft-utilities",
        "nusimdata",
        "root",
    ):
        depends_on(dep)
