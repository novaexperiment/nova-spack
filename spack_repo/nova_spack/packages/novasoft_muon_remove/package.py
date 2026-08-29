from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftMuonRemove(NovasoftPackage):
    """NOvA muon-removal core library."""

    root_cmakelists_dir = "MuonRemove"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "novasoft-cvn",
        "novasoft-geometry",
        "novasoft-geometry-objects",
        "novasoft-numu-sandbox",
        "novasoft-raw-data",
        "novasoft-reco-base",
        "nusimdata",
        "root",
    ):
        depends_on(dep)

    def cmake_args(self):
        args = super().cmake_args()
        args.append(self.define("NOVASOFT_BUILD_MUONREMOVE_MODULES", False))
        args.append(self.define("NOVASOFT_BUILD_MUONREMOVE_GEANT", False))
        return args
