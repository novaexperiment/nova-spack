# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftCovarianceMatrixFit(NovasoftPackage):
    """Covariance-matrix fitting framework and art plugins."""

    root_cmakelists_dir = "CovarianceMatrixFit"

    depends_on("art")
    depends_on("art-root-io")
    depends_on(
        "boost+date_time+filesystem+iostreams+math+program_options+regex"
        "+serialization+system+test+thread"
    )
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("eigen")
    depends_on("fhicl-cpp")
    depends_on("gsl")
    depends_on("messagefacility")
    depends_on("nusimdata")
    depends_on("osclib")
    depends_on("root")
    depends_on("stan-math")
    depends_on("sundials")
    depends_on("tbb")

    def setup_build_environment(self, env):
        super().setup_build_environment(env)
        env.set("STAN_MATH_INC", self.spec["stan-math"].prefix.include)
        env.set("SUNDIALS_INC", self.spec["sundials"].prefix.include)
