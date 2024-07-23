# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import spack
from spack.package import *


class NovaFcl(Package):
    """NOvA experiment FHICL repository"""

    homepage = "https://www.github.com/novaexperiment/novaprod"
    git = "git@github.com:novaexperiment/novaprod"

    maintainers("vhewes")

    version("develop", branch="main")

    def install(self, spec, prefix):
        """nova-fcl installer"""
        ignore = lambda a: "GNUmakefile" in a or "CMakeLists.txt" in a
        copy_tree("novaproduction/fcl", prefix, ignore=ignore)

    def setup_run_environment(self, env):
        """set up nova-fcl run environment"""
        env.set("NOVA_FCL", self.prefix)
