from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftHmatrixE(NovasoftPackage):
    """NOvA HMatrix electron-neutrino reconstruction tools."""

    root_cmakelists_dir = "HMatrixE"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "nova-daq",
        "novasoft-calibrator",
        "novasoft-cmap",
        "novasoft-geometry",
        "novasoft-geometry-objects",
        "novasoft-mccheater",
        "novasoft-raw-data",
        "novasoft-reco-base",
        "novasoft-reco-jm-shower",
        "novasoft-rec-var-pid",
        "novasoft-simulation",
        "novasoft-summary-data",
        "novasoft-utilities",
        "nusimdata",
        "root",
    ):
        depends_on(dep)
