# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftTestBeamSim(NovasoftPackage):
    """Test-beam simulation configuration and helper scripts."""

    root_cmakelists_dir = "TestBeamSim"

    depends_on("art")
    depends_on("art-root-io")
    depends_on("novasoft-beamline-sim")
    depends_on("novasoft-beamline-utils")
    depends_on("novasoft-mccheater")
    depends_on("novasoft-metadata")
    depends_on("novasoft-simulation")
    depends_on("novasoft-test-beam-utils")
    depends_on("nusimdata")
