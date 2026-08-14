# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.nova_spack.build_systems.novasoft import NovasoftPackage
from spack.package import *


class NovasoftDatabase(NovasoftPackage):
    """Database access library and utilities from novasoft."""

    root_cmakelists_dir = "Database"

    depends_on(
        "boost+date_time+filesystem+iostreams+math+program_options+regex"
        "+serialization+system+test+thread"
    )
    depends_on("cetlib")
    depends_on("curl")
    depends_on("libwda")
    depends_on("nova-daq")
    depends_on("postgresql")
    depends_on("xerces-c")
    depends_on("xsd")

    def setup_build_environment(self, env):
        super().setup_build_environment(env)

        env.set("CSTXSD_FQ_DIR", self.spec["xsd"].prefix)
        xsd_version = "v{}".format(self.spec["xsd"].version.underscored)
        env.set("CSTXSD_VERSION", xsd_version)
        env.set("NOVADAQ_FQ_DIR", self.spec["nova-daq"].prefix)
