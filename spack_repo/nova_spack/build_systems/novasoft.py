"""Common build support for packages split from the novasoft monorepo."""

from spack_repo.builtin.build_systems.cmake import CMakePackage, generator
from spack.package import *


class NovasoftPackage(CMakePackage):
    """Base class for independently built novasoft source directories."""

    homepage = "https://github.com/novaexperiment/novasoft"
    git = "git@github.com:novaexperiment/novasoft"

    maintainers("vhewes")

    version("spack-refactor", branch="spack_remastered")

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
    depends_on("cetmodules", type="build")

    generator("ninja")

    def cmake_args(self):
        return [self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd")]

    def setup_build_environment(self, env):
        # Standalone CMake code generation must read the shared monorepo source,
        # not a previously installed monolithic novasoft prefix.
        env.set("NOVASOFT_DIR", self.stage.source_path)

        # External dependencies do not run their dependent-environment hooks.
        # Supply the variables required by the legacy NOvASoft finder here.
        if "cafanacore" in self.spec:
            env.set("CAFANACORE_FQ_DIR", self.spec["cafanacore"].prefix)
            env.set("CAFANACORE_INC", self.spec["cafanacore"].prefix.inc)
