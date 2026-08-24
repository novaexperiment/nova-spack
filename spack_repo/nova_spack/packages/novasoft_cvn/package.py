from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftCvn(NovasoftPackage):
    """Convolutional visual network data products and functions."""

    root_cmakelists_dir = "CVN"

    for dep in (
        "art",
        "boost+system",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "nova-daq",
        "novasoft-mccheater",
        "novasoft-reco-base",
        "nusimdata",
        "root",
    ):
        depends_on(dep)
