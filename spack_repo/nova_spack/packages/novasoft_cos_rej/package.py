from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftCosRej(NovasoftPackage):
    """NOvA cosmic rejection core library."""

    root_cmakelists_dir = "CosRej"

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
        "novasoft-live-geometry",
        "novasoft-geometry-objects",
        "novasoft-mccheater",
        "novasoft-re-mid",
        "novasoft-reco-base",
        "novasoft-track-fit",
        "root",
    ):
        depends_on(dep)

    def cmake_args(self):
        args = super().cmake_args()
        args.append(self.define("NOVASOFT_BUILD_COSREJ_MODULES", False))
        return args
