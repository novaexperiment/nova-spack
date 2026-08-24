from pathlib import Path

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftTensorflowHandler(NovasoftPackage):
    """NOvA TensorFlow and Triton inference handlers."""

    root_cmakelists_dir = "TensorFlowHandler"

    for dep in (
        "eigen",
        "fhicl-cpp",
        "grpc",
        "novasoft-cvn",
        "protobuf",
        "py-tensorflow",
        "triton",
    ):
        depends_on(dep)

    def setup_build_environment(self, env):
        super().setup_build_environment(env)
        site_packages = Path(python_platlib).relative_to(self.prefix)
        tf_dir = self.spec["py-tensorflow"].prefix.join(site_packages).tensorflow
        env.set("TENSORFLOW_INC", tf_dir.include)
        env.set("TENSORFLOW_LIB", tf_dir)
        env.set("TRITON_INC", self.spec["triton"].prefix.include)
        env.set("TRITON_LIB", self.spec["triton"].prefix.lib)
        env.set("GRPC_INC", self.spec["grpc"].prefix.include)
        env.set("GRPC_LIB", self.spec["grpc"].prefix.lib)
