# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


NOVAPROD_VERSIONS = {
    "25.5.6": {
        "commit": "05b0b5d658267e87ab71006419d7063f4425b19c",
    },
    "25.5.5": {
        "commit": "04d6a33abbd47bbb1181ecfee502c717d6dae327",
        "deprecated": True,
    },
    "25.5.4": {
        "commit": "87a04f76a248bfaa9ada943e893caed0b6d57cc5",
        "deprecated": True,
    },
    "25.5.3": {
        "commit": "8b4bfb57aa295fb4f96088aa4f8b3b49e1e376e2",
        "deprecated": True,
    },
    "25.5.2": {
        "commit": "e42579c41ac6c2537cf1b280f55cdb35dbf084ff",
        "deprecated": True,
    },
    "25.5.1": {
        "commit": "8c384e8a8ad761a5ece836e0128dac9cca3364cb",
        "deprecated": True,
    },
    "25.5.0": {
        "commit": "8d00138120e2ddf23010c6689a0a979a8a287aef",
        "deprecated": True,
    },
}

class NovaGridUtils(Package):
    """NOvA experiment grid utilities"""

    homepage = "https://www.github.com/novaexperiment/novaprod"
    git = "git@github.com:novaexperiment/novaprod"

    maintainers("vhewes")

    version("main", branch="main")
    for v, c in NOVAPROD_VERSIONS.items():
        version(v, **c)

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
