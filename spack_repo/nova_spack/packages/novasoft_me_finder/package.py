from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *

class NovasoftMeFinder(NovasoftPackage):
    """NOvA Michel-electron finding module."""
    root_cmakelists_dir = "MEFinder"
    depends_on("art")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("fhicl-cpp")
    depends_on("messagefacility")
    depends_on("novasoft-cmap")
    depends_on("novasoft-geometry")
    depends_on("novasoft-geometry-objects")
    depends_on("novasoft-reco-base")
    depends_on("novasoft-utilities")
    depends_on("novasoft-utilities-func")
