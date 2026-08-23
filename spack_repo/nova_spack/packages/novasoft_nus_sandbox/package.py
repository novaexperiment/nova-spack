from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *

class NovasoftNusSandbox(NovasoftPackage):
    """NOvA neutrino-systematics sandbox products."""
    root_cmakelists_dir = "NusSandbox"
    for dep in ("art", "art-root-io", "canvas", "cetlib", "cetlib-except", "fhicl-cpp",
                "messagefacility", "nova-daq", "novasoft-geometry", "novasoft-reco-base",
                "novasoft-utilities", "root"):
        depends_on(dep)
