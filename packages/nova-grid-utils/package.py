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

    version("main", branch="main")
    version("25.5.0", commit="8d00138120e2ddf23010c6689a0a979a8a287aef")

    depends_on("ifdhc")
    depends_on("nova-env")
    depends_on("py-future")
    depends_on("sam-web-client")

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
        env.set("NOVAGRIDUTILS_VERSION", str(self.version))
