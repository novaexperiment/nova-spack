from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftMcReweight(NovasoftPackage):
    """NOvA Monte Carlo reweighting library and services."""

    root_cmakelists_dir = "MCReweight"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "dk2nudata",
        "fhicl-cpp",
        "genie",
        "messagefacility",
        "novarwgt",
        "novasoft-reco-base",
        "novasoft-utilities-func",
        "nugen",
        "nusimdata",
        "ppfx",
        "root",
    ):
        depends_on(dep)

    depends_on("nufinder", type="build")

    def setup_build_environment(self, env):
        super().setup_build_environment(env)
        env.set("NUFINDER_DIR", self.spec["nufinder"].prefix)
