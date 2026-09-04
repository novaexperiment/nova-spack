from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftHdf5Maker(NovasoftPackage):
    """NOvA StandardRecord-to-HDF5 library, executable, and art module."""

    root_cmakelists_dir = "HDF5Maker"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "hdf5",
        "hep-hpc",
        "messagefacility",
        "novasoft-mccheater",
        "novasoft-metadata",
        "novasoft-reco-base",
        "novasoft-reco-base-hit",
        "novasoft-simulation",
        "novasoft-standard-record",
        "py-pygccxml",
        "root",
    ):
        depends_on(dep)

    depends_on("castxml", type="build")
    depends_on("python", type="build")

    def setup_build_environment(self, env):
        super().setup_build_environment(env)
        env.set("ROOT_INC", self.spec["root"].prefix.include)
        env.set("HEP_HPC_INC", self.spec["hep-hpc"].prefix.include)
        env.set("HDF5_INC", self.spec["hdf5"].prefix.include)
