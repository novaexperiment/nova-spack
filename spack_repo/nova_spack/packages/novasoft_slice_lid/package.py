from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftSliceLid(NovasoftPackage):
    """NOvA SliceLID variable dictionaries and prediction headers."""

    root_cmakelists_dir = "SliceLID"

    for dep in (
        "art",
        "art-root-io",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "nova-daq",
        "novasoft-geometry",
        "novasoft-live-geometry",
        "novasoft-reco-base",
        "novasoft-shower-lid",
        "root",
    ):
        depends_on(dep)
