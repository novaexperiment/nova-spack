# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftNuMagMomentAna(NovasoftPackage):
    """NOvA neutrino magnetic moment CAFAna analysis libraries."""

    root_cmakelists_dir = "NuMagMomentAna"

    depends_on("cafanacore")
    depends_on("genie")
    depends_on("eigen")
    depends_on("novasoft-cafana")
    depends_on("novasoft-nd-ana")
    depends_on("novasoft-standard-record")
    depends_on("novarwgt")
    depends_on("nugen")
    depends_on("py-srproxy")
    depends_on("root")
    depends_on("stan-math")
    depends_on("sundials")
    depends_on("tbb")
