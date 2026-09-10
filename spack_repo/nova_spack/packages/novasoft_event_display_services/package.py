# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftEventDisplayServices(NovasoftPackage):
    """Shared NOvA event-display drawing and navigation services."""

    root_cmakelists_dir = "EventDisplayServices"

    depends_on("art")
    depends_on("canvas")
    depends_on("fhicl-cpp")
    depends_on("nuevdb")
    depends_on("novasoft-geometry")
    depends_on("novasoft-geometry-objects")
    depends_on("novasoft-mccheater")
    depends_on("novasoft-me-finder")
    depends_on("novasoft-reco-base")
    depends_on("nusimdata")
    depends_on("root")
