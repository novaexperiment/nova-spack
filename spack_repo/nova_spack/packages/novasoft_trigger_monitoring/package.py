# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftTriggerMonitoring(NovasoftPackage):
    """NOvA long-readout trigger monitoring module."""

    root_cmakelists_dir = "TriggerMonitoring"

    depends_on("art")
    depends_on("art-root-io")
    depends_on(
        "boost+date_time+filesystem+iostreams+math+program_options+regex"
        "+serialization+system+test+thread"
    )
    depends_on("canvas")
    depends_on("fhicl-cpp")
    depends_on("messagefacility")
    depends_on("nova-daq")
    depends_on("novasoft-cmap")
    depends_on("novasoft-raw-data")
    depends_on("postgresql")
    depends_on("root")
    depends_on("sqlite")
    depends_on("xerces-c")

