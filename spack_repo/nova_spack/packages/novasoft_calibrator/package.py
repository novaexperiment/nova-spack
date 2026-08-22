# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftCalibrator(NovasoftPackage):
    """Detector calibration service from novasoft."""

    root_cmakelists_dir = "Calibrator"

    depends_on("art")
    depends_on("art-root-io")
    depends_on(
        "boost+date_time+filesystem+iostreams+math+program_options+regex"
        "+serialization+system+test+thread"
    )
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("clhep")
    depends_on("fhicl-cpp")
    depends_on("libwda")
    depends_on("messagefacility")
    depends_on("nova-daq")
    depends_on("novasoft-calibration-utils")
    depends_on("novasoft-cmap")
    depends_on("novasoft-database")
    depends_on("novasoft-geometry")
    depends_on("novasoft-geometry-objects")
    depends_on("novasoft-mccheater-core")
    depends_on("novasoft-photon-transport")
    depends_on("novasoft-raw-data")
    depends_on("novasoft-reco-base-hit")
    depends_on("novasoft-run-history")
    depends_on("nusimdata")
    depends_on("postgresql")
    depends_on("root")
    depends_on("xerces-c")
    depends_on("xsd")

    def setup_build_environment(self, env):
        super().setup_build_environment(env)
        env.set("CSTXSD_FQ_DIR", self.spec["xsd"].prefix)
