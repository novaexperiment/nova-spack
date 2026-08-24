from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftDdtPrescaleOffline(NovasoftPackage):
    """Offline DDT prescale modules."""

    root_cmakelists_dir = "DDTPrescaleOffline"

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
        "nusimdata",
        "root",
    ):
        depends_on(dep)
