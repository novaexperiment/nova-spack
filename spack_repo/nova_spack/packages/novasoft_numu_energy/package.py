# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftNumuEnergy(NovasoftPackage):
    """NOvA numu energy reconstruction core library."""

    root_cmakelists_dir = "NumuEnergy"

    depends_on("art")
    depends_on("art-root-io")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("fhicl-cpp")
    depends_on("messagefacility")
    depends_on("novasoft-cos-rej")
    depends_on("novasoft-geometry")
    depends_on("novasoft-geometry-objects")
    depends_on("novasoft-muon-remove")
    depends_on("novasoft-numu-energy-func")
    depends_on("novasoft-re-mid")
    depends_on("novasoft-reco-base")
    depends_on("root")

    def cmake_args(self):
        args = super().cmake_args()
        args.append(self.define("NOVASOFT_BUILD_NUMUENERGY_MODULES", False))
        return args
