# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftBeamlineRecoBase(NovasoftPackage):
    """Beamline reconstruction data products."""

    root_cmakelists_dir = "BeamlineRecoBase"

    depends_on("art")
    depends_on("boost+system")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("messagefacility")
    depends_on("novasoft-beamline-utils")
    depends_on("novasoft-raw-data")
    depends_on("novasoft-reco-base")
    depends_on("root")
