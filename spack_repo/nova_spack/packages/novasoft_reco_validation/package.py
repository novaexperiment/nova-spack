# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftRecoValidation(NovasoftPackage):
    """NOvA reconstruction-validation analyzers and CAF cutter."""

    root_cmakelists_dir = "RecoValidation"

    depends_on("art")
    depends_on("art-root-io")
    depends_on("cafanacore")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("fhicl-cpp")
    depends_on("messagefacility")
    depends_on("novasoft-3-flavor-ana+full")
    depends_on("novasoft-break-point-fitter")
    depends_on("novasoft-cafana")
    depends_on("novasoft-elastic-arms")
    depends_on("novasoft-fuzzy-k-vertex")
    depends_on("novasoft-hough-track")
    depends_on("novasoft-mccheater")
    depends_on("novasoft-nux-ana")
    depends_on("novasoft-raw-data")
    depends_on("novasoft-reco-base")
    depends_on("novasoft-slicer")
    depends_on("novasoft-standard-record")
    depends_on("novasoft-track-fit")
    depends_on("nusimdata")
    depends_on("py-srproxy")
    depends_on("root")
