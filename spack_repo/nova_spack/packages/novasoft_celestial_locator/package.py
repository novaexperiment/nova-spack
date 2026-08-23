# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftCelestialLocator(NovasoftPackage):
    """NOvA celestial-coordinate location service."""

    root_cmakelists_dir = "CelestialLocator"

    depends_on("art")
    depends_on(
        "boost+date_time+filesystem+iostreams+math+program_options+regex"
        "+serialization+system+test+thread"
    )
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("fhicl-cpp")
    depends_on("nova-daq")
    depends_on("postgresql")
    depends_on("root")
    depends_on("xerces-c")

