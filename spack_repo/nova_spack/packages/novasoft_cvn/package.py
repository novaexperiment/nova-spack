# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftCvn(NovasoftPackage):
    """Convolutional visual network data products and functions."""

    root_cmakelists_dir = "CVN"

    depends_on("art")
    depends_on("boost+system")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("fhicl-cpp")
    depends_on("nova-daq")
    depends_on("novasoft-mccheater")
    depends_on("novasoft-reco-base")
    depends_on("nusimdata")
    depends_on("root")
