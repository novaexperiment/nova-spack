from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *

class NovasoftDsoResultPlotter(NovasoftPackage):
    """NOvA DSO result plotting executable."""
    root_cmakelists_dir = "DSOResultPlotter"
    depends_on("boost+date_time+filesystem+system+thread")
    depends_on("nova-daq")
    depends_on("postgresql")
    depends_on("root")
    depends_on("xerces-c")
