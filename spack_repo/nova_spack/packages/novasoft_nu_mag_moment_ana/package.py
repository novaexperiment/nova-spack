from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftNuMagMomentAna(NovasoftPackage):
    """NOvA neutrino magnetic moment CAFAna analysis libraries."""

    root_cmakelists_dir = "NuMagMomentAna"

    for dep in (
        "cafanacore",
        "eigen",
        "novasoft-cafana",
        "novasoft-nd-ana",
        "novasoft-standard-record",
        "novarwgt",
        "py-srproxy",
        "root",
        "stan-math",
        "sundials",
        "tbb",
    ):
        depends_on(dep)
