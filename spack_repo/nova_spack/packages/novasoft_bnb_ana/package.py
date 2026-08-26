from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftBnbAna(NovasoftPackage):
    """NOvA BNB analysis variables, cuts, and weights."""

    root_cmakelists_dir = "BNBAna"

    for dep in (
        "cafanacore",
        "novasoft-3-flavor-ana",
        "novasoft-cafana",
        "novasoft-standard-record",
        "novasoft-utilities",
        "py-srproxy",
        "root",
    ):
        depends_on(dep)
