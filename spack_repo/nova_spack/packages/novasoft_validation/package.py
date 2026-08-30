from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftValidation(NovasoftPackage):
    """NOvA validation art modules and configuration."""

    root_cmakelists_dir = "Validation"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "novasoft-cvn",
        "novasoft-geometry",
        "novasoft-geometry-objects",
        "novasoft-mccheater",
        "novasoft-raw-data",
        "novasoft-reco-base",
        "novasoft-reco-base-hit",
        "novasoft-run-history",
        "novasoft-simulation",
        "novasoft-summary-data",
        "novasoft-utilities-func",
        "nusimdata",
        "root",
    ):
        depends_on(dep)
