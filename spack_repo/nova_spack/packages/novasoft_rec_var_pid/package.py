from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *

class NovasoftRecVarPid(NovasoftPackage):
    """NOvA reconstructed-variable particle identification."""
    root_cmakelists_dir = "RecVarPID"
    depends_on("art")
    depends_on("art-root-io")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("fhicl-cpp")
    depends_on("messagefacility")
    depends_on("nova-daq")
    depends_on("novasoft-calibrator")
    depends_on("novasoft-geometry")
    depends_on("novasoft-reco-base")
    depends_on("novasoft-utilities")
    depends_on("root")
