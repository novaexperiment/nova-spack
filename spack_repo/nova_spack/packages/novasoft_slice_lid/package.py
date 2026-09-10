# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftSliceLid(NovasoftPackage):
    """NOvA SliceLID variable dictionaries and prediction headers."""

    root_cmakelists_dir = "SliceLID"

    depends_on("art")
    depends_on("art-root-io")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("fhicl-cpp")
    depends_on("messagefacility")
    depends_on("nova-daq")
    depends_on("novasoft-geometry")
    depends_on("novasoft-live-geometry")
    depends_on("novasoft-reco-base")
    depends_on("novasoft-shower-lid")
    depends_on("root")

    def setup_build_environment(self, env):
        super().setup_build_environment(env)
        env.set("NOVADAQ_INC", self.spec["nova-daq"].prefix.include)
