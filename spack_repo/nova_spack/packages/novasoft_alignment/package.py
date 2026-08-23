from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *

class NovasoftAlignment(NovasoftPackage):
    """NOvA detector alignment modules."""
    root_cmakelists_dir = "Alignment"
    for dep in ("art", "art-root-io", "canvas", "cetlib", "cetlib-except", "fhicl-cpp",
                "messagefacility", "nova-daq", "novasoft-cmap", "novasoft-geometry",
                "novasoft-geometry-objects", "novasoft-reco-base", "novasoft-track-fit",
                "novasoft-utilities", "root"):
        depends_on(dep)
