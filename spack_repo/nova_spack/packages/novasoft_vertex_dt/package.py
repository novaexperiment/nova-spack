from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *

class NovasoftVertexDt(NovasoftPackage):
    """NOvA distance-transform vertex reconstruction."""
    root_cmakelists_dir = "VertexDT"
    for dep in ("art", "art-root-io", "canvas", "cetlib", "cetlib-except", "fhicl-cpp",
                "messagefacility", "novasoft-channel-info", "novasoft-geometry",
                "novasoft-geometry-objects", "novasoft-reco-base", "novasoft-utilities", "root"):
        depends_on(dep)
