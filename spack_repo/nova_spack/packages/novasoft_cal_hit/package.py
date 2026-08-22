# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftCalHit(NovasoftPackage):
    """Calibrated-hit producer from novasoft."""

    root_cmakelists_dir = "CalHit"

    depends_on("art")
    depends_on("art-root-io")
    depends_on("boost+system+thread")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("fhicl-cpp")
    depends_on("messagefacility")
    depends_on("nova-daq")
    depends_on("novasoft-calibration-func")
    depends_on("novasoft-calibration-utils")
    depends_on("novasoft-calibrator")
    depends_on("novasoft-channel-info")
    depends_on("novasoft-cmap")
    depends_on("novasoft-mccheater")
    depends_on("novasoft-raw-data")
    depends_on("novasoft-reco-base")
    depends_on("novasoft-run-history")
    depends_on("root")
