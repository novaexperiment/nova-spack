# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftProductMorgue(NovasoftPackage):
    """Retired NOvA data-product headers retained for compatibility."""

    root_cmakelists_dir = "ProductMorgue"

    depends_on("canvas")
    depends_on("novasoft-reco-base")
    depends_on("root")
