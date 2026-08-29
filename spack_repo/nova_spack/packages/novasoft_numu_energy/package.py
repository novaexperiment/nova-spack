from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftNumuEnergy(NovasoftPackage):
    """NOvA numu energy reconstruction core library."""

    root_cmakelists_dir = "NumuEnergy"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "novasoft-cos-rej",
        "novasoft-geometry",
        "novasoft-geometry-objects",
        "novasoft-muon-remove",
        "novasoft-numu-energy-func",
        "novasoft-re-mid",
        "novasoft-reco-base",
        "root",
    ):
        depends_on(dep)

    def cmake_args(self):
        args = super().cmake_args()
        args.append(self.define("NOVASOFT_BUILD_NUMUENERGY_MODULES", False))
        return args
