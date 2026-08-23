from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *

class NovasoftXnuePid(NovasoftPackage):
    """NOvA Xnue particle-identification products."""
    root_cmakelists_dir = "XnuePID"
    for dep in ("art", "art-root-io", "canvas", "cetlib", "cetlib-except", "fhicl-cpp",
                "messagefacility", "novasoft-calibrator", "novasoft-geometry",
                "novasoft-rec-var-pid", "novasoft-reco-base", "novasoft-utilities", "root"):
        depends_on(dep)
