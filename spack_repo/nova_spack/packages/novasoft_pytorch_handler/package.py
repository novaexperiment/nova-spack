from pathlib import Path

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftPytorchHandler(NovasoftPackage):
    """NOvA LibTorch inference handler."""

    root_cmakelists_dir = "PyTorchHandler"

    depends_on("fhicl-cpp")
    depends_on("novasoft-cvn")
    depends_on("py-torch")
    depends_on("python")

    def cmake_args(self):
        site_packages = Path(python_platlib).relative_to(self.prefix)
        torch_dir = self.spec["py-torch"].prefix.join(site_packages).torch
        return super().cmake_args() + [
            self.define("Torch_DIR", torch_dir.share.cmake.Torch)
        ]
