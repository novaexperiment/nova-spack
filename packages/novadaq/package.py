# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Novadaq(CMakePackage):
    """NOvA DAQ package"""

    homepage = "https://www.github.com/novaexperiment/novadaq"
    git = "git@github.com:novaexperiment/novadaq"

    root_cmakelists_dir = "pkgs"

    maintainers("vhewes")

    version("18.0.0", branch="R18_00_00_e20")

    variant(
        "cxxstd",
        default="17",
        values=("17", "20", "23"),
        multi=False,
        sticky=True,
        description="C++ standard",
    )

    depends_on("cetmodules", type="build")

    depends_on("boost")
    depends_on("libwda")
    depends_on("messagefacility")
    depends_on("postgresql")
    depends_on("xerces-c")
    depends_on("xsd")

    patch("R18_00_00_e20.patch", when="@18.0.0")

    def cmake_args(self):
        return [self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd")]

    def setup_build_environment(self, env):
      env.set("CSTXSD_FQ_DIR", self.spec["xsd"].prefix)
      xsd_version = "v{}".format(self.spec["xsd"].version.underscored)
      env.set("CSTXSD_VERSION", xsd_version)
