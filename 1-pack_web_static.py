#!/usr/bin/python3
"""This module generates .tgz archive"""

from fabric.api import *
from datetime import datetime


def do_pack():
    """This function archive webstatic folder"""

    # Current date and time
    archive = datetime.now().strftime("web_static_%Y%m%d%H%M%S.tgz")

    # Create the versions directory
    try:
        local("mkdir -p versions")
    except Exception:
        pass

    arch_path = 'versions/{}'.format(archive)

    # Archive the file
    result = local("tar -cvzf {} web_static".format(arch_path))

    if result.succeeded:
        return arch_path
    
    return None
