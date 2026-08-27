from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftXsecReco(NovasoftPackage):
    """NOvA cross-section reconstruction art modules."""

    root_cmakelists_dir = "XSecReco"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "novasoft-calibrator",
        "novasoft-cvn",
        "novasoft-geometry",
        "novasoft-live-geometry",
        "novasoft-geometry-objects",
        "novasoft-mccheater",
        "novasoft-re-mid",
        "novasoft-reco-base",
        "novasoft-shower-lid",
        "novasoft-standard-record",
        "novasoft-timing-fit",
        "novasoft-track-fit",
        "novasoft-utilities",
        "novasoft-utilities-func",
        "root",
    ):
        depends_on(dep)
