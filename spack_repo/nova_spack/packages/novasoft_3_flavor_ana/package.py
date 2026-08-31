from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class Novasoft3FlavorAna(NovasoftPackage):
    """NOvA three-flavor analysis variables and cuts."""

    root_cmakelists_dir = "3FlavorAna"

    variant("full", default=False, description="Build all 3FlavorAna analysis libraries")

    for dep in (
        "boost",
        "cafanacore",
        "eigen",
        "genie",
        "gsl",
        "novarwgt",
        "nugen",
        "novasoft-cafana",
        "novasoft-numu-energy-func",
        "novasoft-standard-record",
        "novasoft-utilities",
        "osclib",
        "py-srproxy",
        "root",
        "stan-math",
        "sundials",
        "tbb",
    ):
        depends_on(dep)

    def cmake_args(self):
        args = super().cmake_args()
        args.append(
            self.define(
                "NOVASOFT_BUILD_3FLAVORANA_FULL", self.spec.satisfies("+full")
            )
        )
        return args
