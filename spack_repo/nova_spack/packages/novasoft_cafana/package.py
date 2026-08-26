from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftCafana(NovasoftPackage):
    """NOvA analysis libraries built on the CAFAna framework."""

    root_cmakelists_dir = "CAFAna"

    for dep in (
        "boost",
        "cafanacore@01.42",
        "eigen",
        "genie",
        "gsl",
        "ifdhc",
        "novarwgt",
        "nugen",
        "novasoft-authentication",
        "novasoft-ncid-func",
        "novasoft-numu-energy-func",
        "novasoft-standard-record",
        "novasoft-utilities",
        "novasoft-utilities-func",
        "osclib",
        "py-pybind11",
        "py-srproxy",
        "python",
        "root",
        "stan",
        "stan-math",
        "sundials",
        "tbb",
    ):
        depends_on(dep)

    def cmake_args(self):
        args = super().cmake_args()
        args.append(
            self.define(
                "CAFANACORE_VERSION", "v{}".format(self.spec["cafanacore"].version)
            )
        )
        return args
