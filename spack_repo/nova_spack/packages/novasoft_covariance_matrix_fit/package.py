from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftCovarianceMatrixFit(NovasoftPackage):
    """Covariance-matrix fitting framework and art plugins."""

    root_cmakelists_dir = "CovarianceMatrixFit"

    for dep in (
        "art",
        "art-root-io",
        "boost+date_time+filesystem+iostreams+math+program_options+regex"
        "+serialization+system+test+thread",
        "canvas",
        "cetlib",
        "cetlib-except",
        "eigen",
        "fhicl-cpp",
        "messagefacility",
        "nusimdata",
        "osclib",
        "root",
    ):
        depends_on(dep)
