from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *

class NovasoftLem(NovasoftPackage):
    """NOvA library event matching reconstruction."""
    root_cmakelists_dir = "LEM"
    for dep in ("art", "art-root-io", "canvas", "cetlib", "cetlib-except", "fhicl-cpp", "ifdhc",
                "messagefacility", "novasoft-calibrator", "novasoft-cmap", "novasoft-geometry",
                "novasoft-geometry-objects", "novasoft-mccheater", "novasoft-metadata",
                "novasoft-raw-data", "novasoft-reco-base", "novasoft-simulation",
                "novasoft-summary-data", "novasoft-utilities", "nusimdata", "root"):
        depends_on(dep)
