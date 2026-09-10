# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.fnal_art.packages.nusystematics.package import (
    Nusystematics as FnalNusystematics,
)
from spack.package import depends_on


class Nusystematics(FnalNusystematics):
    """NuSystematics with dependencies required by current releases."""

    depends_on("eigen@3.4:")
    depends_on("lhapdf")
