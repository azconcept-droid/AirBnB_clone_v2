#!/usr/bin/python3

from fabric import Connection
from datetime import datetime


def do_pack():

    # Current date and time
    archive = datetime.now().strftime("web_static_%Y%m%d%H%M%S.tgz")

    try:
        with Connection(host='localhost') as c:
            # Create the versions directory
            c.local("mkdir -p versions")

            arch_path = 'versions/{}'.format(archive)

            # Archive the file
            c.local("tar -cvzf {} web_static".format(arch_path))

        return arch_path
    except Exception:
        return None
