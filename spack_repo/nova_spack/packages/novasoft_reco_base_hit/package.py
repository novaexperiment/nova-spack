# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftRecoBaseHit(NovasoftPackage):
    """Base reconstructed-hit data products from novasoft."""

    root_cmakelists_dir = "RecoBaseHit"

    depends_on("art")
    depends_on("canvas")
    depends_on("novasoft-geometry-objects")
    depends_on("novasoft-raw-data")
