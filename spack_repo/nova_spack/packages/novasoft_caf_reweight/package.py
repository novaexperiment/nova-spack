# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftCafReweight(NovasoftPackage):
    """NOvA CAF reweighting support."""

    root_cmakelists_dir = "CAFReweight"

    depends_on("art")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("fhicl-cpp")
    depends_on("genie")
    depends_on("libxml2")
    depends_on("log4cpp")
    depends_on("messagefacility")
    depends_on("novasoft-standard-record")
    depends_on("nugen")
    depends_on("root")

    def setup_build_environment(self, env):
        super().setup_build_environment(env)
        env.set("LOG4CPP_INC", self.spec["log4cpp"].prefix.include)
        env.set("LOG4CPP_LIB", self.spec["log4cpp"].prefix.lib)
