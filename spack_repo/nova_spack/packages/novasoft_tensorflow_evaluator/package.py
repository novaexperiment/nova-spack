# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from pathlib import Path

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftTensorflowEvaluator(NovasoftPackage):
    """NOvA TensorFlow-based CVN, SliceLID, and LSTME art modules."""

    root_cmakelists_dir = "TensorFlowEvaluator"

    depends_on("art")
    depends_on("art-root-io")
    depends_on("boost")
    depends_on("canvas")
    depends_on("cetlib")
    depends_on("cetlib-except")
    depends_on("fhicl-cpp")
    depends_on("messagefacility")
    depends_on("nova-daq")
    depends_on("novasoft-cvn")
    depends_on("novasoft-geometry")
    depends_on("novasoft-geometry-objects")
    depends_on("novasoft-live-geometry")
    depends_on("novasoft-lstme")
    depends_on("novasoft-mccheater")
    depends_on("novasoft-re-mid")
    depends_on("novasoft-reco-base")
    depends_on("novasoft-slice-lid")
    depends_on("novasoft-standard-record")
    depends_on("novasoft-summary-data")
    depends_on("novasoft-tensorflow-handler")
    depends_on("novasoft-tensorflow-products")
    depends_on("novasoft-utilities")
    depends_on("novasoft-utilities-func")
    depends_on("py-tensorflow")
    depends_on("python")
    depends_on("root")

    def setup_build_environment(self, env):
        super().setup_build_environment(env)
        site_packages = Path(python_platlib).relative_to(self.prefix)
        tf_dir = self.spec["py-tensorflow"].prefix.join(site_packages).tensorflow
        env.set("TENSORFLOW_INC", tf_dir.include)
        env.set("TENSORFLOW_LIB", tf_dir)
