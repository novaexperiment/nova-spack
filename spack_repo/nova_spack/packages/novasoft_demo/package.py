from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftDemo(NovasoftPackage):
    """NOvA tutorial and demonstration modules."""

    root_cmakelists_dir = "Demo"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "novasoft-mccheater",
        "novasoft-raw-data",
        "novasoft-reco-base",
        "novasoft-reco-base-hit",
        "novasoft-simulation",
        "nusimdata",
        "root",
    ):
        depends_on(dep)
