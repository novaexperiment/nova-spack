from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftNcidFunc(NovasoftPackage):
    """Neural-network classifier helpers from the novasoft monorepo."""

    root_cmakelists_dir = "NCID/func"

    depends_on("root")
