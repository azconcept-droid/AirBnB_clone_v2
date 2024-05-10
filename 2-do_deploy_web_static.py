#!/usr/bin/python3
"""Deployment module"""

from fabric.api import *
import os

env.user = 'ubuntu'
env.hosts = ['18.204.16.142', '54.175.223.202']


def do_deploy(archive_path):
    """Distribute archive web_static to web servers"""

    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        archive_name = archive_path.partition('/')[-1]

        # Source path
        source = "/tmp/{}".format(archive_name)

        # Archive name without extention
        archive_no_ext = archive_name.partition('.')[0]

        # Path to destination
        destination = "/data/web_static/releases/{}" + archive_no_ext

        # Create destination folder
        run("mkdir -p {}".format(destination))

        # Uncompress to destination/web_static folder
        run("tar -xvf {} -C {}".format(source, destination))

        # Move to destination from destination/web_static
        run("mv {}/web_static/* {}".format(destination, destination))

        # Remove /tmp/archive_name
        run("rm {}".format(source))

        # Remove symbolic link if it exist
        run("rm -rf /data/webstatic/current")

        # Create symbolic link to new release
        run("ln -s {} /data/web_static/current".format(destination))

        return True
    except Exception:
        return False
