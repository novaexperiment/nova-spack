# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCondb(Package):
    """Relational conditions database."""

    homepage = "https://github.com/ivmfnal/condb"
    git = "https://github.com/ivmfnal/condb.git"

    maintainers("vhewes")

    version("2.2", commit="5a0afca6aeb6dc8774554e3bb63961dd089f188b")

    depends_on("py-psycopg2")

    extends("python")

    patch("nova-2.2.patch", when="@2.2")

    def install(self, spec, prefix):
        """condb installer"""
        libdir = join_path(python_platlib, "condb")
        mkdirp(libdir)
        install("NOvA_API/*.py", libdir)
