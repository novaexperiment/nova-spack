from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class Novasoft3FlavorAna(NovasoftPackage):
    """NOvA three-flavor analysis variables and cuts."""

    root_cmakelists_dir = "3FlavorAna"

    for dep in (
        "boost",
        "cafanacore",
        "eigen",
        "novarwgt",
        "nugen",
        "novasoft-cafana",
        "novasoft-numu-energy-func",
        "novasoft-standard-record",
        "novasoft-utilities",
        "osclib",
        "py-srproxy",
        "root",
        "stan-math",
        "sundials",
        "tbb",
    ):
        depends_on(dep)
