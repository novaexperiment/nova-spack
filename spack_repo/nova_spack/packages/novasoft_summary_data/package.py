# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftSummaryData(NovasoftPackage):
    """Run, subrun, spill, and exposure summaries from novasoft."""

    root_cmakelists_dir = "SummaryData"

    depends_on("art")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("messagefacility")
    depends_on("nova-daq")
