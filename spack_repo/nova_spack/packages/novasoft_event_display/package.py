# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftEventDisplay(NovasoftPackage):
    """NOvA event-display library and art module."""

    root_cmakelists_dir = "EventDisplay"

    depends_on("art")
    depends_on("art-root-io")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("fhicl-cpp")
    depends_on("messagefacility")
    depends_on("nova-daq")
    depends_on("nuevdb")
    depends_on("novasoft-calibrator")
    depends_on("novasoft-channel-info")
    depends_on("novasoft-cmap")
    depends_on("novasoft-event-display-services")
    depends_on("novasoft-geometry")
    depends_on("novasoft-geometry-objects")
    depends_on("novasoft-live-geometry")
    depends_on("novasoft-mccheater")
    depends_on("novasoft-me-finder")
    depends_on("novasoft-raw-data")
    depends_on("novasoft-reco-base")
    depends_on("novasoft-reco-base-hit")
    depends_on("novasoft-simulation")
    depends_on("novasoft-utilities")
    depends_on("nusimdata")
    depends_on("root")
