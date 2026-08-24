from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftFlatMaker(NovasoftPackage):
    """NOvA flat StandardRecord generation and art module."""

    root_cmakelists_dir = "FlatMaker"

    for dep in (
        "art",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "novasoft-metadata",
        "novasoft-standard-record",
        "py-srproxy",
        "root",
    ):
        depends_on(dep)

    def setup_build_environment(self, env):
        super().setup_build_environment(env)
        env.set("SRPROXY_DIR", self.spec["py-srproxy"].prefix)
