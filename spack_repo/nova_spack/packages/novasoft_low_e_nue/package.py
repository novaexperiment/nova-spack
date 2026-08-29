from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftLowENue(NovasoftPackage):
    """NOvA low-energy nue classifier and training support."""

    root_cmakelists_dir = "LowENue"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "novasoft-cos-rej",
        "novasoft-cvn",
        "novasoft-mc-reweight",
        "novasoft-metadata",
        "novasoft-nd-reco",
        "novasoft-numu-energy",
        "novasoft-preselection",
        "novasoft-raw-data",
        "novasoft-reco-base",
        "novasoft-reco-base-hit",
        "novasoft-reco-jm-shower",
        "novasoft-simulation",
        "novasoft-standard-record",
        "novasoft-track-info",
        "novasoft-utilities",
        "novasoft-utilities-func",
        "novasoft-xsec-reco",
        "nusimdata",
        "root",
    ):
        depends_on(dep)

    def cmake_args(self):
        args = super().cmake_args()
        args.append(self.define("NOVASOFT_BUILD_LOWENUE_TRAINING", False))
        return args
