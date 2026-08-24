from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftEventGenerator(NovasoftPackage):
    """NOvA event-generation modules."""

    root_cmakelists_dir = "EventGenerator"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "nugen",
        "novasoft-cmap",
        "novasoft-geometry",
        "novasoft-mccheater",
        "novasoft-raw-data",
        "novasoft-simulation",
        "novasoft-summary-data",
        "nusimdata",
        "root",
    ):
        depends_on(dep)
