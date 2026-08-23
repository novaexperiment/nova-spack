from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *

class NovasoftAirShower(NovasoftPackage):
    """NOvA air-shower reconstruction modules."""
    root_cmakelists_dir = "AirShower"
    depends_on("art")
    depends_on("art-root-io")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("fhicl-cpp")
    depends_on("messagefacility")
    depends_on("nova-daq")
    depends_on("novasoft-geometry")
    depends_on("novasoft-raw-data")
    depends_on("novasoft-reco-base")
    depends_on("root")
