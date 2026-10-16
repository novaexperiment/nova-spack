# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.fnal_art.packages.genie_xsec.package import (
    GenieXsec as FnalGenieXsec,
)
from spack.package import *

NOVA_TUNE = "N2420i0211b-k250-e1000"


class GenieXsec(FnalGenieXsec):
    """GENIE cross-section splines, with the set NOvA uses.

    UPS novasoft sets up genie_xsec v3_06_00 -q e1000:N2420i0211b:k250
    (ups/product_deps). The fnal_art recipe has only 3.04.00 and no N2420i
    tune, so this adds both. Belongs upstream in fnal_art.
    """

    version(
        "3.06.00",
        sha256="ea17249e6bb3159b27bb865e2a6a0133c3ba20acc8b0232ef8e82d88c40440af",
        url="https://scisoft.fnal.gov/scisoft/packages/genie_xsec/v3_06_00/"
        f"genie_xsec-3.06.00-noarch-{NOVA_TUNE}.tar.bz2",
    )

    # Same as fnal_art's, plus the NOvA tune.
    variant(
        "tune_name",
        default="AR2320i00000-k250-e1000",
        multi=False,
        values=(
            "AR2320i00000-k250-e1000",
            "G1801a00000-k250-e1000",
            "G1802a00000-k250-e1000",
            "G1810a0211a-k250-e1000",
            "G1810a0211b-k250-e1000",
            "G2111a00000-k250-e1000",
            "GDNu2001a00000-k120-e200",
            "N1810j0211a-k250-e1000",
            NOVA_TUNE,
        ),
        when="@3.0:",
        description="Name of genie xsec tune set to install.",
    )

    # The 3.06.00 tarball is the NOvA tune itself; there are no other 3.06.00
    # resources here.
    conflicts(f"tune_name={NOVA_TUNE}", when="@:3.05")
    for _t in ("AR2320i00000-k250-e1000", "G1801a00000-k250-e1000",
               "G1802a00000-k250-e1000", "G1810a0211a-k250-e1000",
               "G1810a0211b-k250-e1000", "G2111a00000-k250-e1000",
               "GDNu2001a00000-k120-e200", "N1810j0211a-k250-e1000"):
        conflicts(f"tune_name={_t}", when="@3.06.00")

    def install(self, spec, prefix):
        if spec.satisfies("@3.06.00"):
            tree = join_path("v3_06_00", "NULL", NOVA_TUNE)
            install_tree(join_path(self.stage.source_path, tree), join_path(prefix, tree))
        else:
            super().install(spec, prefix)
