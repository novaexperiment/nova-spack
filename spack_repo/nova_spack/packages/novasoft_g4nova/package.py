from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftG4nova(NovasoftPackage):
    """NOvA Geant4 detector simulation library and modules."""

    root_cmakelists_dir = "g4nova"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "geant4",
        "messagefacility",
        "novasoft-geometry",
        "novasoft-geometry-objects",
        "novasoft-simulation",
        "novasoft-utilities",
        "nug4",
        "nusimdata",
        "root",
    ):
        depends_on(dep)
