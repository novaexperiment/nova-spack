from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftMuonId(NovasoftPackage):
    """NOvA muon-ID core library."""

    root_cmakelists_dir = "MuonID"

    for dep in (
        "art",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "novasoft-reco-base",
        "root",
    ):
        depends_on(dep)

    def cmake_args(self):
        args = super().cmake_args()
        args.append(self.define("NOVASOFT_BUILD_MUONID_MODULES", False))
        return args
