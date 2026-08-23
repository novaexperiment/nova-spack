from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *

class NovasoftFuzzyKVertex(NovasoftPackage):
    """NOvA fuzzy-k vertex reconstruction."""
    root_cmakelists_dir = "FuzzyKVertex"
    depends_on("art")
    depends_on("art-root-io")
    depends_on("boost")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("fhicl-cpp")
    depends_on("messagefacility")
    depends_on("nova-daq")
    depends_on("novasoft-calibrator")
    depends_on("novasoft-channel-info")
    depends_on("novasoft-geometry")
    depends_on("novasoft-geometry-objects")
    depends_on("novasoft-mccheater")
    depends_on("novasoft-reco-base")
    depends_on("novasoft-reco-base-hit")
    depends_on("novasoft-simulation")
    depends_on("novasoft-utilities")
    depends_on("nusimdata")
    depends_on("root")
