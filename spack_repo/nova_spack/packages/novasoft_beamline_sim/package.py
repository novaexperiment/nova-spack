# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftBeamlineSim(NovasoftPackage):
    """Beamline detector simulation and art modules."""

    root_cmakelists_dir = "BeamlineSim"

    depends_on("art")
    depends_on("art-root-io")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("fhicl-cpp")
    depends_on("messagefacility")
    depends_on("novasoft-beamline-reco-base")
    depends_on("novasoft-beamline-sim-base")
    depends_on("novasoft-beamline-utils")
    depends_on("novasoft-raw-data")
    depends_on("novasoft-utilities")
    depends_on("nusimdata")
    depends_on("root")
    depends_on("xerces-c")
