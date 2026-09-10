# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftMcReweight(NovasoftPackage):
    """NOvA Monte Carlo reweighting library and services."""

    root_cmakelists_dir = "MCReweight"

    depends_on("art")
    depends_on("art-root-io")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("dk2nudata")
    depends_on("fhicl-cpp")
    depends_on("genie")
    depends_on("messagefacility")
    depends_on("novarwgt")
    depends_on("novasoft-reco-base")
    depends_on("novasoft-standard-record")
    depends_on("novasoft-utilities-func")
    depends_on("nugen")
    depends_on("nusimdata")
    depends_on("ppfx")
    depends_on("root")

    depends_on("nufinder", type="build")

    def setup_build_environment(self, env):
        super().setup_build_environment(env)
        env.set("NUFINDER_DIR", self.spec["nufinder"].prefix)
