from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftLstme(NovasoftPackage):
    """NOvA LSTM electron-neutrino variable dictionary support."""

    root_cmakelists_dir = "LSTME"

    for dep in (
        "art",
        "novasoft-reco-base",
        "novasoft-slice-lid",
    ):
        depends_on(dep)
