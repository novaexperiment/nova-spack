from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *

class NovasoftElasticArms(NovasoftPackage):
    """NOvA elastic-arms reconstruction."""
    root_cmakelists_dir = "ElasticArms"
    depends_on("art")
    depends_on("art-root-io")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("fhicl-cpp")
    depends_on("messagefacility")
    depends_on("nova-daq")
    depends_on("novasoft-channel-info")
    depends_on("novasoft-geometry")
    depends_on("novasoft-geometry-objects")
    depends_on("novasoft-mccheater")
    depends_on("novasoft-reco-base")
    depends_on("novasoft-utilities")
    depends_on("nusimdata")
    depends_on("root")
