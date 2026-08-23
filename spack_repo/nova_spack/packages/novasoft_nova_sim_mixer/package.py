from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *

class NovasoftNovaSimMixer(NovasoftPackage):
    """NOvA simulated-event mixing modules."""
    root_cmakelists_dir = "NovaSimMixer"
    for dep in ("art", "art-root-io", "canvas", "cetlib", "cetlib-except", "clhep", "dk2nudata",
                "fhicl-cpp", "messagefacility", "nova-daq", "novasoft-calibrator", "novasoft-cmap",
                "novasoft-geometry", "novasoft-mccheater", "novasoft-metadata", "novasoft-raw-data",
                "novasoft-reco-base", "novasoft-reco-base-hit", "novasoft-simulation", "novasoft-summary-data",
                "novasoft-utilities", "nugen", "nusimdata", "root"):
        depends_on(dep)
