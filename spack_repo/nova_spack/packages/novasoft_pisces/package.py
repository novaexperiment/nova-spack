# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

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

    depends_on("boost")
    depends_on("cafanacore")
    depends_on("eigen")
    depends_on("genie")
    depends_on("gsl")
    depends_on("ifdhc")
    depends_on("novasoft-cafana")
    depends_on("novasoft-standard-record")
    depends_on("osclib")
    depends_on("py-srproxy")
    depends_on("root")
    depends_on("stan-math")
    depends_on("sundials")
    depends_on("tbb")

    depends_on("novasoft-3-flavor-ana+full", when="+full")

    def cmake_args(self):
        args = super().cmake_args()
        args.append(
            self.define("NOVASOFT_BUILD_PISCES_FULL", self.spec.satisfies("+full"))
        )
        return args
