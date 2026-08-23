# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftCalibrationDataProducts(NovasoftPackage):
    """NOvA calibration data products."""

    root_cmakelists_dir = "CalibrationDataProducts"

    depends_on("art")
    depends_on(
        "boost+date_time+filesystem+iostreams+math+program_options+regex"
        "+serialization+system+test+thread"
    )
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("messagefacility")
    depends_on("nova-daq")
    depends_on("novasoft-geometry-objects")
    depends_on("novasoft-reco-base")
    depends_on("novasoft-utilities")
    depends_on("postgresql")
    depends_on("root")
    depends_on("xerces-c")

