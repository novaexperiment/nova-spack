# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class G4numi(CMakePackage):
    """Geant4 simulation for NuMI beamline"""

    homepage = "https://redmine.fnal.gov/projects/numi-beam-sim-g4numi"
    git = "https://cdcvs.fnal.gov/projects/numi-beam-sim-g4numi"

    maintainers("vhewes")

    version("develop", branch="main_modern_g4", get_full_repo=True)
    version("24.10.1", tag="v24.10.1", get_full_repo=True)

    depends_on("cetmodules", type="build")

    depends_on("clhep")
    depends_on("dk2nudata")
    depends_on("geant4")
    depends_on("root")
