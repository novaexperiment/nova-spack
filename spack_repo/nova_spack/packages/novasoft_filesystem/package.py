# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftFilesystem(NovasoftPackage):
    """Filesystem and XRootD helpers from the novasoft monorepo."""

    root_cmakelists_dir = "Filesystem"

    depends_on("cafanacore")
    depends_on("novasoft-authentication")
    depends_on("root")
    depends_on("xrootd")

    def setup_build_environment(self, env):
        super().setup_build_environment(env)

        env.set("CAFANACORE_FQ_DIR", self.spec["cafanacore"].prefix)
        env.set("CAFANACORE_INC", self.spec["cafanacore"].prefix.inc)
