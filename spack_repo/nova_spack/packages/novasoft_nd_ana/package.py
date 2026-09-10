# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftNdAna(NovasoftPackage):
    """NOvA near-detector CAFAna classifiers."""

    root_cmakelists_dir = "NDAna"

    depends_on("cafanacore")
    depends_on("genie")
    depends_on("novasoft-cafana")
    depends_on("novasoft-standard-record")
    depends_on("py-srproxy")
    depends_on("root")
