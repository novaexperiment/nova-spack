from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftCafReweight(NovasoftPackage):
    """NOvA CAF reweighting support."""

    root_cmakelists_dir = "CAFReweight"

    for dep in (
        "art",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "genie",
        "libxml2",
        "log4cpp",
        "messagefacility",
        "novasoft-standard-record",
        "nugen",
        "root",
    ):
        depends_on(dep)

    def setup_build_environment(self, env):
        super().setup_build_environment(env)
        env.set("LOG4CPP_INC", self.spec["log4cpp"].prefix.include)
        env.set("LOG4CPP_LIB", self.spec["log4cpp"].prefix.lib)
