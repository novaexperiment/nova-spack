# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftFlatMaker(NovasoftPackage):
    """NOvA flat StandardRecord generation and art module."""

    root_cmakelists_dir = "FlatMaker"

    depends_on("art")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("fhicl-cpp")
    depends_on("messagefacility")
    depends_on("novasoft-metadata")
    depends_on("novasoft-standard-record")
    depends_on("py-srproxy")
    depends_on("root")

    def setup_build_environment(self, env):
        super().setup_build_environment(env)
        env.set("SRPROXY_DIR", self.spec["py-srproxy"].prefix)
