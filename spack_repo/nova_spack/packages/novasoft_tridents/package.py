from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftTridents(NovasoftPackage):
    """NOvA trident data products and art modules."""

    root_cmakelists_dir = "Tridents"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "novasoft-break-point-fitter",
        "novasoft-geometry",
        "novasoft-geometry-objects",
        "novasoft-mccheater",
        "novasoft-reco-base",
        "novasoft-summary-data",
        "nusimdata",
        "root",
    ):
        depends_on(dep)
