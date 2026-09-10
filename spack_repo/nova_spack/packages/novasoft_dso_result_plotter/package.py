# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftDsoResultPlotter(NovasoftPackage):
    """NOvA DSO result plotting executable."""

    root_cmakelists_dir = "DSOResultPlotter"

    depends_on("boost+date_time+filesystem+system+thread")
    depends_on("nova-daq")
    depends_on("postgresql")
    depends_on("root")
    depends_on("xerces-c")
