from pathlib import Path

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftPytorchEvaluator(NovasoftPackage):
    """NOvA LibTorch-based CVN and transformer-energy art modules."""

    root_cmakelists_dir = "PyTorchEvaluator"

    for dep in (
        "art",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "nova-daq",
        "novasoft-cvn",
        "novasoft-geometry",
        "novasoft-lstme",
        "novasoft-mccheater",
        "novasoft-pytorch-handler",
        "novasoft-reco-base",
        "novasoft-slice-lid",
        "novasoft-summary-data",
        "novasoft-utilities",
        "novasoft-utilities-func",
        "py-torch",
        "python",
    ):
        depends_on(dep)

    def cmake_args(self):
        site_packages = Path(python_platlib).relative_to(self.prefix)
        torch_dir = self.spec["py-torch"].prefix.join(site_packages).torch
        return super().cmake_args() + [
            self.define("Torch_DIR", torch_dir.share.cmake.Torch)
        ]
