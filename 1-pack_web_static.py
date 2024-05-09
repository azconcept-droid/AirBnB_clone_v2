#!/usr/bin/python3
"""Archive module"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Compress and package web_static"""

    archive = datetime.now().strftime("web_static_%Y%m%d%H%M%S.tgz")

    try:
        # Create the versions directory
        local("mkdir -p versions")

        arch_path = 'versions/{}'.format(archive)

        # Archive the file
        local("tar -cvzf {} web_static".format(arch_path))

        return arch_path
    except Exception:
        return None
