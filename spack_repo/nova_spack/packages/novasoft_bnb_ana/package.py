# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftBnbAna(NovasoftPackage):
    """NOvA BNB analysis variables, cuts, and weights."""

    root_cmakelists_dir = "BNBAna"

    depends_on("cafanacore")
    depends_on("novasoft-3-flavor-ana")
    depends_on("novasoft-cafana")
    depends_on("novasoft-standard-record")
    depends_on("novasoft-utilities")
    depends_on("py-srproxy")
    depends_on("root")
