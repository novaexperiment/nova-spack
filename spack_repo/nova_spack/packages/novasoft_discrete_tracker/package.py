from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *

class NovasoftDiscreteTracker(NovasoftPackage):
    """NOvA discrete tracking algorithms."""
    root_cmakelists_dir = "DiscreteTracker"
    for dep in ("art", "art-root-io", "canvas", "cetlib", "cetlib-except", "fhicl-cpp",
                "messagefacility", "nova-daq", "novasoft-channel-info", "novasoft-geometry",
                "novasoft-geometry-objects", "novasoft-raw-data", "novasoft-reco-base",
                "novasoft-utilities", "root"):
        depends_on(dep)
