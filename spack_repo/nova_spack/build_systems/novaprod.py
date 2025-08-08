"""Packages from the novaprod repository"""

from spack.package import *


NOVAPROD_VERSIONS = {
    "25.8.0": {
        "commit": "fcab59218dc7b10fb98958a1f612fe46607e10c3",
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
    "25.6.3": {
        "commit": "7e1c0d8ea2e1e4a1dbf24530697adb259cf46a35",
        "deprecated": True,
    },
    "25.6.1": {
        "commit": "7766ccddb0ac35990bddaffc1f10fb942f5523b3",
        "deprecated": True,
    },
    "25.6.0": {
        "commit": "663112eb004f432fd687098e4c5734aa095dc676",
        "deprecated": True,
    },
    "25.5.7": {
        "commit": "e81ccdaeff6fdeee891464e6d3982e5c9dd8988a",
        "deprecated": True,
    },
    "25.5.6": {
        "commit": "05b0b5d658267e87ab71006419d7063f4425b19c",
        "deprecated": True,
    },
    "25.5.5": {
        "commit": "04d6a33abbd47bbb1181ecfee502c717d6dae327",
        "deprecated": True,
    },
    "25.5.4": {
        "commit": "87a04f76a248bfaa9ada943e893caed0b6d57cc5",
        "deprecated": True,
    },
    "25.5.3": {
        "commit": "8b4bfb57aa295fb4f96088aa4f8b3b49e1e376e2",
        "deprecated": True,
    },
    "25.5.2": {
        "commit": "e42579c41ac6c2537cf1b280f55cdb35dbf084ff",
        "deprecated": True,
    },
    "25.5.1": {
        "commit": "8c384e8a8ad761a5ece836e0128dac9cca3364cb",
        "deprecated": True,
    },
    "25.5.0": {
        "commit": "8d00138120e2ddf23010c6689a0a979a8a287aef",
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
