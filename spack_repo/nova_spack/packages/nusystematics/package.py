from spack_repo.fnal_art.packages.nusystematics.package import (
    Nusystematics as FnalNusystematics,
)
from spack.package import depends_on


class Nusystematics(FnalNusystematics):
    """NuSystematics with dependencies required by current releases."""

    depends_on("eigen@3.4:")
    depends_on("lhapdf")
