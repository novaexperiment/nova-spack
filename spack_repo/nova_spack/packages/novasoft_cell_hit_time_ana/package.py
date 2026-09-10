# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftCellHitTimeAna(NovasoftPackage):
    """NOvA cell-hit timing analysis module."""

    root_cmakelists_dir = "CellHitTimeAna"

    depends_on("art")
    depends_on("art-root-io")
    depends_on("cafanacore")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("fhicl-cpp")
    depends_on("messagefacility")
    depends_on("novasoft-3-flavor-ana")
    depends_on("novasoft-calibrator")
    depends_on("novasoft-geometry")
    depends_on("novasoft-geometry-objects")
    depends_on("novasoft-numu-energy-func")
    depends_on("novasoft-re-mid")
    depends_on("novasoft-reco-base")
    depends_on("novasoft-slicer")
    depends_on("novasoft-standard-record")
    depends_on("novasoft-utilities-func")
    depends_on("root")
