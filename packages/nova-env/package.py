# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os

class NovaEnv(BundlePackage):
    """Package to set up NOvA environment"""

    version("develop")

    def setup_run_environment(self, env):
        """set up NOvA environment"""

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

        # database env vars
        env.set("NOVADBHOST", "ifdb12.fnal.gov") # replication host
        env.set("NOVADBHOST1", "ifdb11.fnal.gov") # production host

        # If IS_OFFSITE is not set, then running onsite so can use http.
        if os.environ.get("IS_OFFSITE"):
            # non-cached 8092 -- onsite-only
            env.set("NOVADBWSURL", "http://novacon-data.fnal.gov:8091/NOvACon/v2_2b/app/")
            env.set("NOVADBWSURLINT", "http://novacon-data.fnal.gov:8091/NOvACon/v2_2b/app/")
            env.set("NOVADBWSURLPUT", "http://novacon-data.fnal.gov:8107/NOvACon/v2_2b/app/")
            # non-cached 8106 -- onsite-only
            env.set("NOVADBQEURL", "http://novacon-data.fnal.gov:8105/QE/NOvA/app/SQ/")
        else:
            # non-cached 9443
            env.set("NOVADBWSURL", "https://novacon-data.fnal.gov:8444/NOvACon/v2_2b/app/")
            env.set("NOVADBWSURLINT", "https://novacon-data.fnal.gov:8444/NOvACon/v2_2b/app/")
            env.set("NOVADBWSURLPUT", "https://dbdata0vm.fnal.gov:9443/NOvACon/v2_2b/app/")
            env.set("NOVADBQEURL", "https://dbdata0vm.fnal.gov:9444/QE/NOvA/app/SQ/")

        env.set("NOVAHWDBQEURL", "https://dbdata0vm.fnal.gov:9443/QE/hw/app/SQ/")
        env.set("NOVADBNAME", "nova_prod")
        env.set("NOVADBUSER", "nova_reader")
        env.set("NOVADBPWDFILE", "/cvmfs/nova-development.opensciencegrid.org/novasoft/config/nova_reader_pwd")
        env.set("NOVADBGRIDPWDFILE", "/cvmfs/nova-development.opensciencegrid.org/novasoft/config/nova_grid_pwd")
        env.set("NOVADBWSPWDFILE", "/exp/nova/app/db/nova_devdbws_pwd")
        env.set("NOVADBPORT", "5433")
        env.set("NOVAHWDBHOST", "ifdb12.fnal.gov")
        env.set("NOVAHWDBHOST1", "ifdb11.fnal.gov")
        env.set("NOVAHWDBNAME", "nova_hardware")
        env.set("NOVAHWDBUSER", "nova_reader")
        env.set("NOVAHWDBPORT", "5453")
        env.set("NOVADBTIMEOUT", "30")
        env.set("NOVANEARDAQDBHOST", "ifdb12.fnal.gov")
        env.set("NOVANEARDAQDBNAME", "nova_prod")
        env.set("NOVANEARDAQDBPORT", "5434")
        env.set("NOVANEARDAQDBUSER", "nova_reader")
        env.set("NOVAFARDAQDBHOST", "ifdb12.fnal.gov")
        env.set("NOVAFARDAQDBNAME", "nova_prod")
        env.set("NOVAFARDAQDBPORT", "5438")
        env.set("NOVAFARDAQDBUSER", "nova_reader")
        env.set("NOVAFARDCSDBHOST", "ifdb12.fnal.gov")
        env.set("NOVAFARDCSDBNAME", "nova_prod")
        env.set("NOVAFARDCSDBPORT", "5437")
        env.set("NOVAFARDCSDBUSER", "nova_reader")
