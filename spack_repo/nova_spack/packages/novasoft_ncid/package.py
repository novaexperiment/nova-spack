from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftNcid(NovasoftPackage):
    """NOvA neutral-current ID core library."""

    root_cmakelists_dir = "NCID"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "novasoft-mccheater",
        "novasoft-reco-base",
        "nusimdata",
        "root",
    ):
        depends_on(dep)

    def cmake_args(self):
        args = super().cmake_args()
        args.append(self.define("NOVASOFT_BUILD_NCID_MODULES", False))
        return args
