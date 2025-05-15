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

    version("main", branch="main")
    version("spack-develop", branch="spack-develop")
    version("S25-03-19", tag="S25-03-19")

    variant(
        "cxxstd",
        default="17",
        values=("17", "20", "23"),
        multi=False,
        sticky=True,
        description="C++ standard",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("castxml", type="build")
    depends_on("cetmodules", type="build")
    depends_on("ninja", type="build")
    depends_on("py-pygccxml", type="build")

    depends_on("art")
    depends_on("boost+iostreams+math+serialization")
    depends_on("cafanacore")
    depends_on("geant4")#, patches=[
        # patch("geant4-11-0-carbon-excitation-energy.patch", when="@11.0"),
        # patch("geant4-11-0-em-instance-counter.patch", when="@11.0")])
    depends_on("geant4reweight experiment=nova")
    depends_on("genie")
    depends_on("ifdh-art")
    depends_on("ifdhc")
    depends_on("libwda")
    depends_on("log4cpp")
    depends_on("nova-env")
    depends_on("nova-daq")
    depends_on("nova-reweight")
    depends_on("nucondb")
    depends_on("nuevdb")
    depends_on("nufinder")
    depends_on("nug4")
    depends_on("nugen")
    depends_on("nusimdata")
    depends_on("nusystematics")
    depends_on("nutools")
    depends_on("opencv +imgcodecs")
    depends_on("postgresql")
    depends_on("ppfx")
    depends_on("protobuf")
    depends_on("python")
    depends_on("py-matplotlib")
    depends_on("py-numpy")
    depends_on("py-oracledb")
    depends_on("py-pandas")
    depends_on("py-psycopg2")
    depends_on("py-pybind11")
    depends_on("py-scipy")
    depends_on("py-srproxy")
    depends_on("py-tensorflow")
    depends_on("py-torch")
    depends_on("py-tqdm")
    depends_on("py-uproot")
    depends_on("py-urllib3")
    depends_on("root+spectrum+tmva+xrootd")
    depends_on("stan")

    generator("ninja")

    def cmake_args(self):
        cafanacore_version = "v{}".format(self.spec["cafanacore"].version)
        return [
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            self.define("CAFANACORE_VERSION", cafanacore_version),
        ]

    def setup_build_environment(self, env):
        env.set("NOVASOFT_DIR", self.spec.prefix)

        # gsl
        env.set("GSL_INC", self.spec["gsl"].prefix.include)
        env.set("GSL_LIB", self.spec["gsl"].prefix.lib)

        # castxml
        env.set("CASTXML_DIR", self.spec["castxml"].prefix)
        env.set("CASTXML_FQ_DIR", self.spec["castxml"].prefix)

        # root
        env.set("ROOT_INC", self.spec["root"].prefix.include)

        # xsd
        env.set("CSTXSD_FQ_DIR", self.spec["xsd"].prefix)
        xsd_version = "v{}".format(self.spec["xsd"].version.underscored)
        env.set("CSTXSD_VERSION", xsd_version)

        # novarwgt
        env.set("NOVARWGT_INC", self.spec["nova-reweight"].prefix.inc)
        env.set("NOVARWGT_LIB", self.spec["nova-reweight"].prefix.lib)

        # stan
        env.set("STAN_MATH_INC", self.spec["stan-math"].prefix)
        env.set("STAN_INC", self.spec["stan"].prefix.include)

        # srproxy
        env.set("SRPROXY_DIR", self.spec["py-srproxy"].prefix)
        env.set("SRPROXY_INC", self.spec["py-srproxy"].prefix.include)

        # cafanacore
        env.set("CAFANACORE_FQ_DIR", self.spec["cafanacore"].prefix)
        env.set("CAFANACORE_INC", self.spec["cafanacore"].prefix.inc)

        # get python site_packages path
        site_packages = Path(python_platlib).relative_to(self.prefix)

        # tensorflow
        tf_dir = self.spec["py-tensorflow"].prefix.join(site_packages).tensorflow
        env.set("TENSORFLOW_INC", tf_dir.include)
        env.set("TENSORFLOW_LIB", tf_dir)

        # pytorch
        torch_dir = self.spec["py-torch"].prefix.join(site_packages).torch
        env.set("LIBTORCH_INC", torch_dir.include)
    
    def setup_run_environment(self, env):
        env.set("NOVASOFT_DIR", self.prefix)
        cafanacore_version = "v{}".format(self.spec["cafanacore"].version)
        env.set("CAFANACORE_VERSION", cafanacore_version)

