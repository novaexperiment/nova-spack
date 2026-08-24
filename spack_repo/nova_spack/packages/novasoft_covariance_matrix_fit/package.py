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
        "gsl",
        "messagefacility",
        "nusimdata",
        "osclib",
        "root",
        "stan-math",
        "sundials",
        "tbb",
    ):
        depends_on(dep)

    def setup_build_environment(self, env):
        super().setup_build_environment(env)
        env.set("STAN_MATH_INC", self.spec["stan-math"].prefix.include)
        env.set("SUNDIALS_INC", self.spec["sundials"].prefix.include)
