# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os

class NovaGridUtils(Package):
    """NOvA grid utilities"""

    homepage = "https://www.github.com/novaexperiment/novaprod"
    git = "git@github.com:novaexperiment/novaprod"

    maintainers("vhewes")

    version("develop", branch="main")

    depends_on("py-future")
    depends_on("sam-web-client")
    depends_on("ifdhc")

    extends("python")

    def install(self, spec, prefix):
        """novagridutils installer"""
        mkdirp(prefix.bin, python_platlib)

        # binaries
        install("NovaGridUtils/bin/setup_fnal_security", prefix.bin)
        install("NovaGridUtils/bin/testrel_tarball", prefix.bin)
        install("NovaGridUtils/bin/cache_state.py", prefix.bin)
        install("NovaGridUtils/bin/dropbox_path", prefix.bin)
        install("NovaGridUtils/bin/sl7-nova", prefix.bin)
        install("NovaGridUtils/bin/submit_cafana.py", prefix.bin)
        install("NovaGridUtils/bin/cafe_grid_script.sh", prefix.bin)
        install("NovaGridUtils/bin/submit_nova_art.py", prefix.bin)
        install("NovaGridUtils/bin/art_sam_wrap.sh", prefix.bin)
        install("NovaGridUtils/bin/stashcache.sh", prefix.bin)
        install("NovaGridUtils/bin/submit_production_jobs.py", prefix.bin)
        install("NovaGridUtils/bin/which_fts", prefix.bin)
        install("NovaGridUtils/bin/concat_scripts/*", prefix.bin)
        install("novaproduction/bin/samweb2xrootd", prefix.bin)
        install("novaproduction/bin/pnfs2xrootd", prefix.bin)
        install("novaproduction/bin/prodjob-summary", prefix.bin)
        install("novaproduction/bin/make_genie_job_fcls", prefix.bin)
        install("novaproduction/bin/submit_concat_project.py", prefix.bin)

        # python libraries
        install("NovaGridUtils/lib/python/NovaGridUtils.py", python_platlib)
        install("NovaGridUtils/bin/recommended_sites.py", python_platlib)
        install("novaproduction/lib/python/fake_sam.py", python_platlib)
        install("novaproduction/lib/python/progbar.py", python_platlib)
        install("novaproduction/lib/python/redirect_allout.py", python_platlib)

        # configuration files
        mkdirp(prefix.configs.station, prefix.keepup.ConfigFile)
        install("NovaGridUtils/configs/station/*.cfg", prefix.configs.station)
        install("novaproduction/keepup/ConfigFile/*.cfg", prefix.keepup.ConfigFile)

    def setup_run_environment(self, env):
        """set up novagridutils run environment"""
        # UPS-style NGU env vars
        env.set("NOVAGRIDUTILS_DIR", self.prefix)
        env.set("NOVAGRIDUTILS_VERSION", self.version)

        # config directories
        env.set("NOVA_ART_CONFIG", self.prefix.configs.station)
        env.set("NOVA_KEEPUP_CONFIG", self.prefix.keepup.ConfigFile)

        # jobsub env vars
        env.set("GROUP", "nova")
        env.set("EXPERIMENT", "nova")
        env.set("IFDH_DEBUG", "0")
        env.set("SAM_STATION", "nova")
        env.set("CONDOR_EXEC", f"/exp/nova/app/condor-exec/{os.environ.get('USER')}")
        env.set("IFDH_BASE_URI", "http://samweb.fnal.gov:8480/sam/nova/api")
