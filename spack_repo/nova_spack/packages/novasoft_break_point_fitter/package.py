from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftBreakPointFitter(NovasoftPackage):
    """NOvA break-point fitting data products and reusable algorithms."""

    root_cmakelists_dir = "BreakPointFitter"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "novasoft-calibrator",
        "novasoft-geometry",
        "novasoft-geometry-objects",
        "novasoft-reco-base",
        "novasoft-reco-base-hit",
        "root",
    ):
        depends_on(dep)
