from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *

class NovasoftReadoutSim(NovasoftPackage):
    """NOvA detector readout simulation."""
    root_cmakelists_dir = "ReadoutSim"
    for dep in ("art", "art-root-io", "canvas", "cetlib", "cetlib-except", "clhep", "fhicl-cpp",
                "messagefacility", "nova-daq", "novasoft-channel-info", "novasoft-cmap",
                "novasoft-geometry", "novasoft-geometry-objects", "novasoft-mccheater",
                "novasoft-raw-data", "novasoft-reco-base", "novasoft-run-history",
                "novasoft-simulation", "novasoft-summary-data", "novasoft-utilities",
                "nusimdata", "root"):
        depends_on(dep)
