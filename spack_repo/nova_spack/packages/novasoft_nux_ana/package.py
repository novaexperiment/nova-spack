# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftNuxAna(NovasoftPackage):
    """NOvA sterile-neutrino and nonstandard-interaction analysis libraries."""

    root_cmakelists_dir = "NuXAna"

    depends_on("boost")
    depends_on("cafanacore")
    depends_on("eigen")
    depends_on("genie")
    depends_on("gsl")
    depends_on("ifdhc")
    depends_on("novasoft-3-flavor-ana+full")
    depends_on("novasoft-cafana")
    depends_on("novasoft-nu-mag-moment-ana")
    depends_on("novasoft-numu-energy-func")
    depends_on("novasoft-pisces+full")
    depends_on("novasoft-standard-record")
    depends_on("novasoft-utilities")
    depends_on("nugen")
    depends_on("osclib")
    depends_on("py-srproxy")
    depends_on("root")
    depends_on("stan-math")
    depends_on("sundials")
    depends_on("tbb")
