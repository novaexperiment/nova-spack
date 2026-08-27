from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftReMid(NovasoftPackage):
    """NOvA reconstructed muon identifier core library."""

    root_cmakelists_dir = "ReMId"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "novasoft-calibrator",
        "novasoft-geometry",
        "novasoft-geometry-objects",
        "novasoft-qe-event-finder",
        "novasoft-reco-base",
        "novasoft-utilities",
        "root",
    ):
        depends_on(dep)

    def cmake_args(self):
        args = super().cmake_args()
        args.append(self.define("NOVASOFT_BUILD_REMID_MODULES", False))
        return args
