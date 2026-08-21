# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftCalibrationFunc(NovasoftPackage):
    """Core calibration functions from novasoft."""

    root_cmakelists_dir = "Calibration/func"

    depends_on(
        "boost+date_time+filesystem+iostreams+math+program_options+regex"
        "+serialization+system+test+thread"
    )
    depends_on("fhicl-cpp")
    depends_on("libwda")
    depends_on("messagefacility")
    depends_on("nova-daq")
    depends_on("postgresql")
    depends_on("root")
    depends_on("xerces-c")
    depends_on("xsd")

    def setup_build_environment(self, env):
        super().setup_build_environment(env)
        env.set("CSTXSD_FQ_DIR", self.spec["xsd"].prefix)
        env.set("NOVADAQ_INC", self.spec["nova-daq"].prefix.include)
