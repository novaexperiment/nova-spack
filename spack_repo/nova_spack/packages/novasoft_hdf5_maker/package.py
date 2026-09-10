# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftHdf5Maker(NovasoftPackage):
    """NOvA StandardRecord-to-HDF5 library, executable, and art module."""

    root_cmakelists_dir = "HDF5Maker"

    depends_on("art")
    depends_on("art-root-io")
    depends_on("cafanacore")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("fhicl-cpp")
    depends_on("hdf5")
    depends_on("hep-hpc")
    depends_on("messagefacility")
    depends_on("novasoft-mccheater")
    depends_on("novasoft-metadata")
    depends_on("novasoft-reco-base")
    depends_on("novasoft-reco-base-hit")
    depends_on("novasoft-simulation")
    depends_on("novasoft-standard-record")
    depends_on("py-pygccxml")
    depends_on("root")

    depends_on("castxml", type="build")
    depends_on("python", type="build")

    def setup_build_environment(self, env):
        super().setup_build_environment(env)
        env.set("ROOT_INC", self.spec["root"].prefix.include)
        env.set("HEP_HPC_INC", self.spec["hep-hpc"].prefix.include)
        env.set("HDF5_INC", self.spec["hdf5"].prefix.include)
