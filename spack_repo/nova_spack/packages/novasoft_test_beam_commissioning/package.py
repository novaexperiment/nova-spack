from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftTestBeamCommissioning(NovasoftPackage):
    """NOvA test-beam commissioning modules."""

    root_cmakelists_dir = "TestBeamCommissioning"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "ifdh-art",
        "ifdhc",
        "messagefacility",
        "nova-daq",
        "novasoft-beamline-reco-base",
        "novasoft-beamline-utils",
        "novasoft-cmap",
        "novasoft-geometry",
        "novasoft-geometry-objects",
        "novasoft-live-geometry",
        "novasoft-raw-data",
        "novasoft-reco-base",
        "novasoft-reco-base-hit",
        "novasoft-summary-data",
        "novasoft-test-beam",
        "novasoft-test-beam-utils",
        "nusimdata",
        "root",
    ):
        depends_on(dep)
