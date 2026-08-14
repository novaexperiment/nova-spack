# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftAuthentication(NovasoftPackage):
    """Authentication helpers from the novasoft monorepo."""

    root_cmakelists_dir = "Authentication"

    depends_on("ifdhc")
