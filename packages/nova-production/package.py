# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import spack

class NovaProduction(Package):
    """NOvA experiment production tools"""

    homepage = "https://www.github.com/novaexperiment/novaprod"
    git = "git@github.com:novaexperiment/novaprod"

    maintainers("vhewes")

    version("main", branch="main")

    depends_on("nova-grid-utils")

    extends("python")

    def install(self, spec, prefix):
        """nova-production installer"""
        ignore = lambda a: a in ("lib", "fcl", "ups") or "CMakeLists.txt" in a or "GNUmakefile" in a
        copy_tree("novaproduction", prefix, ignore=ignore)

        # python libraries
        mkdirp(python_platlib)
        install("novaproduction/lib/python/*.py", python_platlib)

    def setup_run_environment(self, env):
        """set up nova-production run environment"""

        env.set("NOVAPRODUCTION_DIR", self.prefix)
        env.set("NOVAPRODUCTION_VERSION", self.version)
