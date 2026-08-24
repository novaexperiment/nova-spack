from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftG4Rwgt(NovasoftPackage):
    """NOvA Geant4 reweighting data products and modules."""

    root_cmakelists_dir = "G4Rwgt"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "dk2nudata",
        "dk2nugenie",
        "fhicl-cpp",
        "messagefacility",
        "nova-daq",
        "novasoft-calibrator",
        "novasoft-geometry",
        "novasoft-geometry-objects",
        "novasoft-mccheater",
        "novasoft-reco-base",
        "novasoft-reco-base-hit",
        "novasoft-simulation",
        "novasoft-utilities",
        "nusimdata",
        "root",
    ):
        depends_on(dep)

    depends_on("geant4reweight experiment=nova")
    depends_on("nufinder", type="build")

    def setup_build_environment(self, env):
        super().setup_build_environment(env)
        env.set("NUFINDER_DIR", self.spec["nufinder"].prefix)
