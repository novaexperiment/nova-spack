from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftNeutronMcAna(NovasoftPackage):
    """NOvA neutron Monte Carlo analysis module."""

    root_cmakelists_dir = "NeutronMCAna"

    for dep in (
        "art",
        "art-root-io",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "novasoft-geometry",
        "novasoft-geometry-objects",
        "novasoft-mccheater",
        "novasoft-numu-energy",
        "novasoft-re-mid",
        "novasoft-reco-base",
        "novasoft-simulation",
        "nusimdata",
        "root",
    ):
        depends_on(dep)
