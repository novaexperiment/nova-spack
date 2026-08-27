from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftNdAna(NovasoftPackage):
    """NOvA near-detector CAFAna classifiers."""

    root_cmakelists_dir = "NDAna"

    for dep in (
        "cafanacore",
        "genie",
        "novasoft-cafana",
        "novasoft-standard-record",
        "py-srproxy",
        "root",
    ):
        depends_on(dep)
