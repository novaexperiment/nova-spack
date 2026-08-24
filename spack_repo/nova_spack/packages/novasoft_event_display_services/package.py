from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftEventDisplayServices(NovasoftPackage):
    """Shared NOvA event-display drawing and navigation services."""

    root_cmakelists_dir = "EventDisplayServices"

    for dep in (
        "art",
        "canvas",
        "fhicl-cpp",
        "nuevdb",
        "novasoft-geometry",
        "novasoft-geometry-objects",
        "novasoft-mccheater",
        "novasoft-me-finder",
        "novasoft-reco-base",
        "nusimdata",
        "root",
    ):
        depends_on(dep)
