from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *

class NovasoftLightModel(NovasoftPackage):
    """NOvA detector light-model selection module."""
    root_cmakelists_dir = "LightModel"
    depends_on("art")
    depends_on("art-root-io")
    depends_on("canvas")
    depends_on("nova-daq")
    depends_on("novasoft-calibration-data-products")
    depends_on("novasoft-calibration-utils")
    depends_on("novasoft-calibrator")
    depends_on("novasoft-channel-info")
    depends_on("novasoft-geometry")
    depends_on("novasoft-geometry-objects")
    depends_on("novasoft-live-geometry")
    depends_on("novasoft-mccheater")
    depends_on("novasoft-reco-base")
    depends_on("novasoft-reco-base-hit")
    depends_on("novasoft-simulation")
    depends_on("novasoft-summary-data")
    depends_on("novasoft-utilities")
    depends_on("nusimdata")
    depends_on("root")
