from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *

class NovasoftGenieSnova(NovasoftPackage):
    """NOvA supernova GENIE flux generation tools."""
    root_cmakelists_dir = "GenieSNova"
    for dep in ("boost", "cetlib", "cetlib-except", "fhicl-cpp", "genie", "gsl", "lhapdf",
                "libxml2", "log4cpp", "messagefacility", "nusimdata", "pythia6", "root"):
        depends_on(dep)
