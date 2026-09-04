from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftOnlineMonitoring(NovasoftPackage):
    """NOvA online-monitoring libraries, tools, viewer, and art module."""

    root_cmakelists_dir = "OnlineMonitoring"

    for dep in (
        "art",
        "art-root-io",
        "boost+regex+system+thread",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "nova-daq",
        "novasoft-cmap",
        "novasoft-geometry",
        "novasoft-geometry-objects",
        "novasoft-raw-data",
        "novasoft-simulation",
        "novasoft-utilities",
        "novasoft-utilities-func",
        "root",
    ):
        depends_on(dep)
