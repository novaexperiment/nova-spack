from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftCosmicStudies(NovasoftPackage):
    """NOvA cosmic-study libraries and art modules."""

    root_cmakelists_dir = "CosmicStudies"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "nugen",
        "novasoft-break-point-fitter",
        "novasoft-geometry",
        "novasoft-geometry-objects",
        "novasoft-reco-base",
        "novasoft-utilities",
        "root",
    ):
        depends_on(dep)
