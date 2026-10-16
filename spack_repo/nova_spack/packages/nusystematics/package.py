# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.fnal_art.packages.nusystematics.package import (
    Nusystematics as FnalNusystematics,
)
from spack.package import *


class Nusystematics(FnalNusystematics):
    """NuSystematics with dependencies required by current releases."""

    # The version UPS novarwgt v4.0-dev6 sets up. Over 02.00.05 it adds the
    # oneSigmaShifts novarwgt needs in DIRT2.EmissEngine.Config.fcl, and
    # response_helper.hh looks fcl #includes up on FHICL_FILE_PATH instead of
    # the current directory.
    version("02.00.07", sha256="3198323d65022b2e977cd2c811175a19dd6809730c6552ce7ffb63ef54c8c1f4")

    depends_on("eigen@3.4:")
    depends_on("lhapdf")

    with when("@=02.00.07"):
        depends_on("systematicstools @02.00.03")

    @run_after("install")
    def install_fcl(self):
        # Upstream CMake installs fcl/ only from 0caa26b8 (develop, 2026-01),
        # which no tag up to v02_00_07 contains. UPS ships it.
        fcl = join_path(self.stage.source_path, "fcl")
        if os.path.isdir(fcl) and not os.path.isdir(self.prefix.fcl):
            install_tree(fcl, self.prefix.fcl)

    def setup_run_environment(self, env):
        env.prepend_path("FHICL_FILE_PATH", self.prefix.fcl)
