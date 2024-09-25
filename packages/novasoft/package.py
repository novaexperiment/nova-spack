# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Novasoft(CMakePackage):
    """NOvA offline code repository."""

    homepage = "https://www.github.com/novaexperiment/novasoft"
    git = "git@github.com:novaexperiment/novasoft"

    maintainers("vhewes")

    version("develop", branch="main")

    variant(
        "cxxstd",
        default="17",
        values=("17", "20", "23"),
        multi=False,
        sticky=True,
        description="C++ standard",
    )

    depends_on("cetmodules", type="build")

    depends_on("art")
    depends_on("boost+iostreams+math+serialization")
    depends_on("cafanacore")
    depends_on("geant4")
    depends_on("geant4reweight experiment=nova")
    depends_on("ifdh-art")
    depends_on("ifdhc")
    depends_on("libwda")
    depends_on("log4cpp")
    depends_on("nova-env")
    depends_on("novadaq")
    depends_on("novarwgt")
    depends_on("nuevdb")
    depends_on("nufinder")
    depends_on("nug4")
    depends_on("nugen")
    depends_on("nusimdata")
    depends_on("postgresql")
    depends_on("ppfx")
    depends_on("root+spectrum+tmva")
    depends_on("stan")

    depends_on("py-matplotlib")
    depends_on("py-numpy")
    depends_on("py-oracledb")
    depends_on("py-pandas")
    depends_on("py-psycopg2")
    depends_on("py-pybind11")
    depends_on("py-scipy")
    depends_on("py-srproxy")
    depends_on("py-urllib3")

    def setup_build_environment(self, env):
        env.set("STAN_MATH_INC", self.spec["stan-math"].prefix)
        env.set("STAN_INC", self.spec["stan"].prefix.include)
        env.set("CAFANACORE_INC", self.spec["cafanacore"].prefix.inc)
        env.set("NOVARWGT_INC", self.spec["novarwgt"].prefix.inc)
