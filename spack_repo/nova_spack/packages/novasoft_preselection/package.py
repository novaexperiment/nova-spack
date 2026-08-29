from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftPreselection(NovasoftPackage):
    """NOvA preselection data products and core veto objects."""

    root_cmakelists_dir = "Preselection"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "novasoft-calibrator",
        "novasoft-cos-rej",
        "novasoft-geometry",
        "novasoft-live-geometry",
        "novasoft-geometry-objects",
        "novasoft-mccheater",
        "novasoft-reco-base",
        "novasoft-summary-data",
        "novasoft-utilities",
        "novasoft-utilities-func",
        "nusimdata",
        "root",
    ):
        depends_on(dep)

    def cmake_args(self):
        args = super().cmake_args()
        args.append(self.define("NOVASOFT_BUILD_PRESELECTION_MODULES", False))
        return args
