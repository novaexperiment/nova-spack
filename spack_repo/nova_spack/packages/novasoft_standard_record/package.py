# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftStandardRecord(NovasoftPackage):
    """StandardRecord data model and proxy libraries from novasoft."""

    root_cmakelists_dir = "StandardRecord"

    depends_on("art")
    depends_on("genie")
    depends_on("nufinder", type="build")
    depends_on("novarwgt")
    depends_on("nugen")
    depends_on("py-srproxy")
    depends_on("root")

    def setup_build_environment(self, env):
        super().setup_build_environment(env)

        env.set("ROOT_INC", self.spec["root"].prefix.include)
        env.set("NUFINDER_DIR", self.spec["nufinder"].prefix)
        env.set("SRPROXY_DIR", self.spec["py-srproxy"].prefix)
        env.set("SRPROXY_INC", self.spec["py-srproxy"].prefix.include)

