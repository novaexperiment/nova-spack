from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftRecoValidation(NovasoftPackage):
    """NOvA reconstruction-validation analyzers and CAF cutter."""

    root_cmakelists_dir = "RecoValidation"

    for dep in (
        "art",
        "art-root-io",
        "cafanacore",
        "canvas",
        "cetlib",
        "cetlib-except",
        "fhicl-cpp",
        "messagefacility",
        "novasoft-3-flavor-ana+full",
        "novasoft-break-point-fitter",
        "novasoft-cafana",
        "novasoft-elastic-arms",
        "novasoft-fuzzy-k-vertex",
        "novasoft-hough-track",
        "novasoft-mccheater",
        "novasoft-nux-ana",
        "novasoft-raw-data",
        "novasoft-reco-base",
        "novasoft-slicer",
        "novasoft-standard-record",
        "novasoft-track-fit",
        "nusimdata",
        "py-srproxy",
        "root",
    ):
        depends_on(dep)
