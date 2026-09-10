# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftLowENue(NovasoftPackage):
    """NOvA low-energy nue classifier and training support."""

    root_cmakelists_dir = "LowENue"

    depends_on("art")
    depends_on("art-root-io")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("fhicl-cpp")
    depends_on("messagefacility")
    depends_on("novasoft-cos-rej")
    depends_on("novasoft-cvn")
    depends_on("novasoft-mc-reweight")
    depends_on("novasoft-metadata")
    depends_on("novasoft-nd-reco")
    depends_on("novasoft-numu-energy")
    depends_on("novasoft-preselection")
    depends_on("novasoft-raw-data")
    depends_on("novasoft-reco-base")
    depends_on("novasoft-reco-base-hit")
    depends_on("novasoft-reco-jm-shower")
    depends_on("novasoft-simulation")
    depends_on("novasoft-standard-record")
    depends_on("novasoft-track-info")
    depends_on("novasoft-utilities")
    depends_on("novasoft-utilities-func")
    depends_on("novasoft-xsec-reco")
    depends_on("nusimdata")
    depends_on("root")

    def cmake_args(self):
        args = super().cmake_args()
        args.append(self.define("NOVASOFT_BUILD_LOWENUE_TRAINING", False))
        return args
