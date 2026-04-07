"""Packages from the novaprod repository"""

from spack.package import *


NOVAPROD_VERSIONS = {
    "26.4.0": {
        "commit": "cc1f732833a52247f7efcc7265ad339de8721139",
    },
    "25.10.0": {
        "commit": "4c19d292c05f376d48118fd03a362c1ee5454ca7",
        "deprecated": True,
    },
    "25.8.1": {
        "commit": "852558192fde93600dbc98b25f282222a660d442",
        "deprecated": True,
    },
    "25.8.0": {
        "commit": "fcab59218dc7b10fb98958a1f612fe46607e10c3",
        "deprecated": True,
    },
    "25.7.2": {
        "commit": "f673b9c9afefab30ae94c01a035cd93ae35e95b3",
        "deprecated": True,
    },
    "25.7.1": {
        "commit": "1d1c10d70e4684d669aac6b6c36459ab3749c195",
        "deprecated": True,
    },
    "25.7.0": {
        "commit": "09bdadf1f92a2b90d91b0aaaae94632d3fe69f8f",
        "deprecated": True,
    },
}

class NovaprodPackage(Package):
    """Parent class for packages from the novaprod repository"""

    homepage = "https://www.github.com/novaexperiment/novaprod"
    git = "git@github.com:novaexperiment/novaprod"

    maintainers("vhewes")

    version("main", branch="main")
    for v, c in NOVAPROD_VERSIONS.items():
        version(v, **c)
