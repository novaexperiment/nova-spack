from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftQeEventFinder(NovasoftPackage):
    """NOvA QE event finder core PID library."""

    root_cmakelists_dir = "QEEventFinder"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "novasoft-geometry",
        "novasoft-reco-base",
        "root",
    ):
        depends_on(dep)

    def cmake_args(self):
        args = super().cmake_args()
        args.append(self.define("NOVASOFT_BUILD_QEEVENTFINDER_MODULES", False))
        return args
