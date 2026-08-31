from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftPisces(NovasoftPackage):
    """Core PISCES covariance and oscillation-analysis library."""

    root_cmakelists_dir = "PISCES"

    variant(
        "full",
        default=False,
        description="Build PISCES Experiment, Plot, and Systs libraries",
    )

    for dep in (
        "boost",
        "cafanacore",
        "eigen",
        "genie",
        "gsl",
        "ifdhc",
        "novasoft-cafana",
        "novasoft-standard-record",
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
            self.define("NOVASOFT_BUILD_PISCES_FULL", self.spec.satisfies("+full"))
        )
        return args
