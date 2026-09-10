# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from pathlib import Path

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftPytorchEvaluator(NovasoftPackage):
    """NOvA LibTorch-based CVN and transformer-energy art modules."""

    root_cmakelists_dir = "PyTorchEvaluator"

    depends_on("art")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("fhicl-cpp")
    depends_on("messagefacility")
    depends_on("nova-daq")
    depends_on("novasoft-cvn")
    depends_on("novasoft-geometry")
    depends_on("novasoft-lstme")
    depends_on("novasoft-mccheater")
    depends_on("novasoft-pytorch-handler")
    depends_on("novasoft-reco-base")
    depends_on("novasoft-slice-lid")
    depends_on("novasoft-summary-data")
    depends_on("novasoft-utilities")
    depends_on("novasoft-utilities-func")
    depends_on("py-torch")
    depends_on("python")

    def cmake_args(self):
        site_packages = Path(python_platlib).relative_to(self.prefix)
        torch_dir = self.spec["py-torch"].prefix.join(site_packages).torch
        return super().cmake_args() + [
            self.define("Torch_DIR", torch_dir.share.cmake.Torch)
        ]
