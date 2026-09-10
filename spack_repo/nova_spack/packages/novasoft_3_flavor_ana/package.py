# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class Novasoft3FlavorAna(NovasoftPackage):
    """NOvA three-flavor analysis variables and cuts."""

    root_cmakelists_dir = "3FlavorAna"

    variant("full", default=False, description="Build all 3FlavorAna analysis libraries")

    depends_on("boost")
    depends_on("cafanacore")
    depends_on("eigen")
    depends_on("genie")
    depends_on("gsl")
    depends_on("novarwgt")
    depends_on("nugen")
    depends_on("novasoft-cafana")
    depends_on("novasoft-numu-energy-func")
    depends_on("novasoft-standard-record")
    depends_on("novasoft-utilities")
    depends_on("osclib")
    depends_on("py-srproxy")
    depends_on("root")
    depends_on("stan-math")
    depends_on("sundials")
    depends_on("tbb")

    def cmake_args(self):
        args = super().cmake_args()
        args.append(
            self.define(
                "NOVASOFT_BUILD_3FLAVORANA_FULL", self.spec.satisfies("+full")
            )
        )
        return args
