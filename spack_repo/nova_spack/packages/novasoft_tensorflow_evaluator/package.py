from pathlib import Path

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftTensorflowEvaluator(NovasoftPackage):
    """NOvA TensorFlow-based CVN, SliceLID, and LSTME art modules."""

    root_cmakelists_dir = "TensorFlowEvaluator"

    for dep in (
        "art",
        "art-root-io",
        "boost",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "nova-daq",
        "novasoft-cvn",
        "novasoft-geometry",
        "novasoft-geometry-objects",
        "novasoft-live-geometry",
        "novasoft-lstme",
        "novasoft-mccheater",
        "novasoft-re-mid",
        "novasoft-reco-base",
        "novasoft-slice-lid",
        "novasoft-standard-record",
        "novasoft-summary-data",
        "novasoft-tensorflow-handler",
        "novasoft-tensorflow-products",
        "novasoft-utilities",
        "novasoft-utilities-func",
        "py-tensorflow",
        "python",
        "root",
    ):
        depends_on(dep)

    def setup_build_environment(self, env):
        super().setup_build_environment(env)
        site_packages = Path(python_platlib).relative_to(self.prefix)
        tf_dir = self.spec["py-tensorflow"].prefix.join(site_packages).tensorflow
        env.set("TENSORFLOW_INC", tf_dir.include)
        env.set("TENSORFLOW_LIB", tf_dir)
