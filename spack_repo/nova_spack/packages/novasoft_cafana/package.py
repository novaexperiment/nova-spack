# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftCafana(NovasoftPackage):
    """NOvA analysis libraries built on the CAFAna framework."""

    root_cmakelists_dir = "CAFAna"

    depends_on("boost")
    depends_on("cafanacore@01.42")
    depends_on("eigen")
    depends_on("genie")
    depends_on("gsl")
    depends_on("ifdhc")
    depends_on("novarwgt")
    depends_on("nugen")
    depends_on("novasoft-authentication")
    depends_on("novasoft-ncid-func")
    depends_on("novasoft-numu-energy-func")
    depends_on("novasoft-standard-record")
    depends_on("novasoft-utilities")
    depends_on("novasoft-utilities-func")
    depends_on("osclib")
    depends_on("py-pybind11")
    depends_on("py-srproxy")
    depends_on("python")
    depends_on("root")
    depends_on("stan")
    depends_on("stan-math")
    depends_on("sundials")
    depends_on("tbb")

    def cmake_args(self):
        args = super().cmake_args()
        args.append(
            self.define(
                "CAFANACORE_VERSION", "v{}".format(self.spec["cafanacore"].version)
            )
        )
        return args
