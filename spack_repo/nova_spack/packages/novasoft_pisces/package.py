from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftPisces(NovasoftPackage):
    """Core PISCES covariance and oscillation-analysis library."""

    root_cmakelists_dir = "PISCES"

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
