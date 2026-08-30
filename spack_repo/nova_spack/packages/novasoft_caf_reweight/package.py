from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftCafReweight(NovasoftPackage):
    """NOvA CAF reweighting support."""

    root_cmakelists_dir = "CAFReweight"

    for dep in (
        "art",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "genie",
        "log4cpp",
        "messagefacility",
        "novasoft-standard-record",
        "nugen",
        "root",
    ):
        depends_on(dep)
