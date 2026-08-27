from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftShowerLid(NovasoftPackage):
    """NOvA shower likelihood identification algorithms."""

    root_cmakelists_dir = "ShowerLID"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "clhep",
        "eigen",
        "fhicl-cpp",
        "messagefacility",
        "nova-daq",
        "novasoft-calibrator",
        "novasoft-geometry",
        "novasoft-geometry-objects",
        "novasoft-reco-base",
        "novasoft-utilities",
        "novasoft-utilities-func",
        "root",
    ):
        depends_on(dep)

    def cmake_args(self):
        args = super().cmake_args()
        args.append(self.define("NOVASOFT_BUILD_SHOWERLID_FULL", False))
        return args
