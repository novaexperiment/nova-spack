from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftNuxAna(NovasoftPackage):
    """NOvA sterile-neutrino and nonstandard-interaction analysis libraries."""

    root_cmakelists_dir = "NuXAna"

    for dep in (
        "boost",
        "cafanacore",
        "eigen",
        "genie",
        "gsl",
        "ifdhc",
        "novasoft-3-flavor-ana+full",
        "novasoft-cafana",
        "novasoft-nu-mag-moment-ana",
        "novasoft-numu-energy-func",
        "novasoft-pisces+full",
        "novasoft-standard-record",
        "novasoft-utilities",
        "nugen",
        "osclib",
        "py-srproxy",
        "root",
        "stan-math",
        "sundials",
        "tbb",
    ):
        depends_on(dep)
