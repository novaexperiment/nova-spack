from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftG4Standalone(NovasoftPackage):
    """Standalone Geant4 testbed for NOvA detector geometries."""

    root_cmakelists_dir = "G4StandAlone"

    depends_on("clhep")
    depends_on("geant4")
    depends_on("root")

    def cmake_args(self):
        return super().cmake_args() + [
            self.define("WITH_G4NU", False),
            self.define("WITH_GEANT4_UIVIS", False),
        ]
