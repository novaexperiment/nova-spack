# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftNovaSimMixer(NovasoftPackage):
    """NOvA simulated-event mixing modules."""

    root_cmakelists_dir = "NovaSimMixer"

    depends_on("art")
    depends_on("art-root-io")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("clhep")
    depends_on("dk2nudata")
    depends_on("dk2nugenie")
    depends_on("fhicl-cpp")
    depends_on("messagefacility")
    depends_on("nova-daq")
    depends_on("novasoft-calibrator")
    depends_on("novasoft-cmap")
    depends_on("novasoft-geometry")
    depends_on("novasoft-mccheater")
    depends_on("novasoft-metadata")
    depends_on("novasoft-raw-data")
    depends_on("novasoft-reco-base")
    depends_on("novasoft-reco-base-hit")
    depends_on("novasoft-simulation")
    depends_on("novasoft-summary-data")
    depends_on("novasoft-utilities")
    depends_on("nugen")
    depends_on("nusimdata")
    depends_on("root")

    depends_on("nufinder", type="build")

    def setup_build_environment(self, env):
        super().setup_build_environment(env)
        env.set("NUFINDER_DIR", self.spec["nufinder"].prefix)
