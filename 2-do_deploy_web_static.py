#!/usr/bin/python3
"""Deployment module"""

from fabric.api import run, put

env.user = 'ubuntu'
env.hosts = ['18.204.16.142', '54.175.223.202']


def do_deploy(archive_path):
    """Distribute archive web_static to web servers"""

    if archive_path is None:
        return False

    try:
        put(archive_path, "/tmp/")

        archive_part = archive_path.partition('/')

        archive_name = archive_part[1]

        source = "/tmp/{}".format(archive_path)

        destination = "/data/web_static/releases/".format(archive_name)

        run("mkdir -p /data/web_satic/releases")
        run("tar -xvf {} -C {}".format(source, destination))

        run("rm {}".format(archive_path))
        run("rm -rf /data/web_static/current")
        run("link -s {} /data/web_static/current".format(destination))

        return True
    except Exception:
        return False

