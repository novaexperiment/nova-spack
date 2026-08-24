from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftCalibration(NovasoftPackage):
    """NOvA calibration services, modules, and utilities."""

    root_cmakelists_dir = "Calibration"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "nova-daq",
        "novasoft-calibration-data-products",
        "novasoft-calibration-func",
        "novasoft-calibration-utils",
        "novasoft-calibrator",
        "novasoft-channel-info",
        "novasoft-cmap",
        "novasoft-database",
        "novasoft-geometry",
        "novasoft-geometry-objects",
        "novasoft-live-geometry",
        "novasoft-mccheater",
        "novasoft-me-finder",
        "novasoft-photon-transport",
        "novasoft-raw-data",
        "novasoft-reco-base",
        "novasoft-run-history",
        "novasoft-simulation",
        "novasoft-summary-data",
        "novasoft-utilities",
        "novasoft-utilities-func",
        "nusimdata",
        "root",
        "sqlite",
    ):
        depends_on(dep)
