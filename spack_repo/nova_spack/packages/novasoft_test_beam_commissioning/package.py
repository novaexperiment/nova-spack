# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftTestBeamCommissioning(NovasoftPackage):
    """NOvA test-beam commissioning modules."""

    root_cmakelists_dir = "TestBeamCommissioning"

    depends_on("art")
    depends_on("art-root-io")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("fhicl-cpp")
    depends_on("ifdh-art")
    depends_on("ifdhc")
    depends_on("messagefacility")
    depends_on("nova-daq")
    depends_on("novasoft-beamline-reco-base")
    depends_on("novasoft-beamline-utils")
    depends_on("novasoft-cmap")
    depends_on("novasoft-geometry")
    depends_on("novasoft-geometry-objects")
    depends_on("novasoft-live-geometry")
    depends_on("novasoft-raw-data")
    depends_on("novasoft-reco-base")
    depends_on("novasoft-reco-base-hit")
    depends_on("novasoft-summary-data")
    depends_on("novasoft-test-beam")
    depends_on("novasoft-test-beam-utils")
    depends_on("nusimdata")
    depends_on("root")
