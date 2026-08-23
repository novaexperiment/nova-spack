from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *

class NovasoftShowerE(NovasoftPackage):
    """NOvA shower-energy analysis modules."""
    root_cmakelists_dir = "ShowerE"
    depends_on("art")
    depends_on("art-root-io")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("fhicl-cpp")
    depends_on("messagefacility")
    depends_on("novasoft-calibrator")
    depends_on("novasoft-geometry")
    depends_on("novasoft-geometry-objects")
    depends_on("novasoft-mccheater")
    depends_on("novasoft-reco-base")
    depends_on("novasoft-simulation")
    depends_on("novasoft-utilities-func")
    depends_on("nusimdata")
    depends_on("root")
