# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftCalibrationUtils(NovasoftPackage):
    """Calibration utility library from novasoft."""

    root_cmakelists_dir = "CalibrationUtils"

    depends_on("art")
    depends_on("art-root-io")
    depends_on("canvas")
    depends_on("messagefacility")
    depends_on("nova-daq")
    depends_on("novasoft-channel-info")
    depends_on("novasoft-cmap")
    depends_on("novasoft-geometry")
    depends_on("novasoft-live-geometry")
    depends_on("novasoft-utilities")
    depends_on("nusimdata")
    depends_on("root")

    def setup_build_environment(self, env):
        super().setup_build_environment(env)
        env.set("NOVADAQ_INC", self.spec["nova-daq"].prefix.include)
