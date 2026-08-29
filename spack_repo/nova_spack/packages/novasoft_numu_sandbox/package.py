from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftNumuSandbox(NovasoftPackage):
    """NOvA numu sandbox core data products."""

    root_cmakelists_dir = "NumuSandbox"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "novasoft-geometry",
        "novasoft-live-geometry",
        "novasoft-geometry-objects",
        "novasoft-mccheater",
        "novasoft-reco-base",
        "novasoft-track-fit",
        "root",
    ):
        depends_on(dep)

    def cmake_args(self):
        args = super().cmake_args()
        args.append(self.define("NOVASOFT_BUILD_NUMUSANDBOX_MODULES", False))
        return args
