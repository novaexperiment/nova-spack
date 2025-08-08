# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novaprod import NovaprodPackage
from spack.package import *


class NovaFcl(NovaprodPackage):
    """NOvA experiment FHICL repository"""

    def install(self, spec, prefix):
        """nova-fcl installer"""
        ignore = lambda a: "GNUmakefile" in a or "CMakeLists.txt" in a
        copy_tree("novaproduction/fcl", prefix, ignore=ignore)

    def setup_run_environment(self, env):
        """set up nova-fcl run environment"""
        env.set("NOVA_FCL", self.prefix)
