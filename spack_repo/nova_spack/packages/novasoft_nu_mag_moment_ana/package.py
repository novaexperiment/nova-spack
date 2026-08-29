from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftNuMagMomentAna(NovasoftPackage):
    """NOvA neutrino magnetic moment CAFAna analysis libraries."""

    root_cmakelists_dir = "NuMagMomentAna"

    for dep in (
        "cafanacore",
        "novasoft-cafana",
        "novasoft-nd-ana",
        "novasoft-standard-record",
        "py-srproxy",
        "root",
    ):
        depends_on(dep)
