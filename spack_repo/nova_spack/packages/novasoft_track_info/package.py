from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftTrackInfo(NovasoftPackage):
    """NOvA track information core library."""

    root_cmakelists_dir = "TrackInfo"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "novasoft-break-point-fitter",
        "novasoft-geometry",
        "novasoft-live-geometry",
        "novasoft-geometry-objects",
        "novasoft-mccheater",
        "novasoft-reco-base",
        "nusimdata",
        "root",
    ):
        depends_on(dep)

    def cmake_args(self):
        args = super().cmake_args()
        args.append(self.define("NOVASOFT_BUILD_TRACKINFO_MODULES", False))
        return args
