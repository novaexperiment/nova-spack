from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *

class NovasoftTrackFit(NovasoftPackage):
    """NOvA track fitting algorithms and modules."""
    root_cmakelists_dir = "TrackFit"
    for dep in ("art", "art-root-io", "canvas", "cetlib", "cetlib-except", "fhicl-cpp",
                "messagefacility", "nova-daq", "novasoft-calibrator", "novasoft-channel-info",
                "novasoft-cmap", "novasoft-geometry", "novasoft-geometry-objects",
                "novasoft-live-geometry", "novasoft-mccheater", "novasoft-raw-data",
                "novasoft-reco-base", "novasoft-simulation",
                "novasoft-utilities", "nusimdata", "root"):
        depends_on(dep)
