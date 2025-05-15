# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import spack

VERSIONS = {
    "25.5.0": "8d00138120e2ddf23010c6689a0a979a8a287aef",
}

class NovaProduction(Package):
    """NOvA experiment production tools"""

    homepage = "https://www.github.com/novaexperiment/novaprod"
    git = "git@github.com:novaexperiment/novaprod"

    maintainers("vhewes")

    version("main", branch="main")
    for v, c in VERSIONS.items():
        version(v, commit=c)
        depends_on(f"nova-grid-utils@{v}", when=f"@{v}")

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
        env.set("NOVAPRODUCTION_VERSION", str(self.version))
