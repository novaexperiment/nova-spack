# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftTestBeam(NovasoftPackage):
    """Test-beam analysis modules and shared selection code."""

    root_cmakelists_dir = "TestBeam"

    depends_on("art")
    depends_on("art-root-io")
    depends_on(
        "boost+date_time+filesystem+iostreams+math+program_options+regex"
        "+serialization+system+test+thread"
    )
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("fhicl-cpp")
    depends_on("ifdh-art")
    depends_on("messagefacility")
    depends_on("nova-daq")
    depends_on("novasoft-beamline-reco")
    depends_on("novasoft-beamline-reco-base")
    depends_on("novasoft-beamline-sim-base")
    depends_on("novasoft-beamline-utils")
    depends_on("novasoft-channel-info")
    depends_on("novasoft-cmap")
    depends_on("novasoft-geometry")
    depends_on("novasoft-geometry-objects")
    depends_on("novasoft-mccheater")
    depends_on("novasoft-metadata")
    depends_on("novasoft-raw-data")
    depends_on("novasoft-reco-base")
    depends_on("novasoft-reco-base-hit")
    depends_on("novasoft-simulation")
    depends_on("novasoft-summary-data")
    depends_on("novasoft-test-beam-utils")
    depends_on("nusimdata")
    depends_on("postgresql")
    depends_on("root")
    depends_on("xerces-c")
