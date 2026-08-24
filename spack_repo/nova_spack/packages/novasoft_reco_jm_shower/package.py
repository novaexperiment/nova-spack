from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftRecoJmShower(NovasoftPackage):
    """NOvA JM shower reconstruction core."""

    root_cmakelists_dir = "RecoJMShower"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "clhep",
        "fhicl-cpp",
        "messagefacility",
        "nova-daq",
        "novasoft-geometry",
        "novasoft-geometry-objects",
        "novasoft-mccheater",
        "novasoft-reco-base",
        "nusimdata",
        "root",
    ):
        depends_on(dep)
