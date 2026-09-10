# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftG4nova(NovasoftPackage):
    """NOvA Geant4 detector simulation library and modules."""

    root_cmakelists_dir = "g4nova"

    depends_on("art")
    depends_on("art-root-io")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("fhicl-cpp")
    depends_on("geant4")
    depends_on("messagefacility")
    depends_on("novasoft-geometry")
    depends_on("novasoft-geometry-objects")
    depends_on("novasoft-simulation")
    depends_on("novasoft-utilities")
    depends_on("nug4")
    depends_on("nusimdata")
    depends_on("root")

    depends_on("nufinder", type="build")

    def setup_build_environment(self, env):
        super().setup_build_environment(env)
        env.set("NUFINDER_DIR", self.spec["nufinder"].prefix)
