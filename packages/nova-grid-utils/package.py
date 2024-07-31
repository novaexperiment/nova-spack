# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os

class NovaGridUtils(Package):
    """NOvA experiment grid utilities"""

    homepage = "https://www.github.com/novaexperiment/novaprod"
    git = "git@github.com:novaexperiment/novaprod"

    maintainers("vhewes")

    version("develop", branch="main")

    depends_on("py-future")
    depends_on("sam-web-client")
    depends_on("ifdhc")

    extends("python")

    def install(self, spec, prefix):
        """nova-grid-utils installer"""
        ignore = lambda a: a in ("lib", "ups") or "CMakeLists.txt" in a
        copy_tree("NovaGridUtils", prefix, ignore=ignore)

        # python libraries
        mkdirp(python_platlib)
        install("NovaGridUtils/lib/python/*.py", python_platlib)

    def setup_run_environment(self, env):
        """set up nova-grid-utils run environment"""

        env.set("NOVAGRIDUTILS_DIR", self.prefix)
        env.set("NOVAGRIDUTILS_VERSION", self.version)

        # config directories
        env.set("NOVA_ART_CONFIG", self.prefix.configs)
        env.set("NOVA_ART_CONFIG_BASE", self.prefix.configs.base)
        env.set("NOVA_ART_CONFIG_STATION", self.prefix.configs.station)
        env.set("NOVA_KEEPUP_CONFIG", self.prefix.keepup.ConfigFile)

        # jobsub env vars
        env.set("GROUP", "nova")
        env.set("EXPERIMENT", "nova")
        env.set("IFDH_DEBUG", "0")
        env.set("SAM_STATION", "nova")
        env.set("CONDOR_EXEC", "/exp/nova/app/condor-exec/"+os.environ.get("USER"))
        env.set("IFDH_BASE_URI", "http://samweb.fnal.gov:8480/sam/nova/api")
