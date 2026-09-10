# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftPreselection(NovasoftPackage):
    """NOvA preselection data products and core veto objects."""

    root_cmakelists_dir = "Preselection"

    depends_on("art")
    depends_on("art-root-io")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("fhicl-cpp")
    depends_on("messagefacility")
    depends_on("novasoft-calibrator")
    depends_on("novasoft-cos-rej")
    depends_on("novasoft-geometry")
    depends_on("novasoft-live-geometry")
    depends_on("novasoft-geometry-objects")
    depends_on("novasoft-mccheater")
    depends_on("novasoft-reco-base")
    depends_on("novasoft-summary-data")
    depends_on("novasoft-utilities")
    depends_on("novasoft-utilities-func")
    depends_on("nusimdata")
    depends_on("root")

    def cmake_args(self):
        args = super().cmake_args()
        args.append(self.define("NOVASOFT_BUILD_PRESELECTION_MODULES", False))
        return args
