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

        archive_name= archive_path.partition('/')[-1]

        source = "/tmp/{}".format(archive_name)

        # archive name without extention
        archive_no_ext = archive_name.partition('.')[0]

        destination = "/data/web_static/releases/".format(archive_no_ext)

        run("tar -xvf {} -C {}".format(source, destination))

        run("rm {}".format(source))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(destination))

        return True
    except Exception:
        return False
