from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftEventDisplay(NovasoftPackage):
    """NOvA event-display library and art module."""

    root_cmakelists_dir = "EventDisplay"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "nova-daq",
        "nuevdb",
        "novasoft-calibrator",
        "novasoft-channel-info",
        "novasoft-cmap",
        "novasoft-event-display-services",
        "novasoft-geometry",
        "novasoft-geometry-objects",
        "novasoft-live-geometry",
        "novasoft-mccheater",
        "novasoft-me-finder",
        "novasoft-raw-data",
        "novasoft-reco-base",
        "novasoft-reco-base-hit",
        "novasoft-simulation",
        "novasoft-utilities",
        "nusimdata",
        "root",
    ):
        depends_on(dep)
