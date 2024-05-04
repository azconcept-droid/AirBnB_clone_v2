#!/usr/bin/python3
"""This module generates .tgz archive"""

from fabric import *
from sys import argv

env.user = argv[2]

env.sshkey = argv[1]

env.hosts = ['18.204.16.142', '54.175.223.202']


def do_deploy(archive_path):
    """This function archive webstatic folder"""

    if archive_path is None:
        return False

    try:
        put(archive_path, "/tmp/")

        archive_name = archive_path.partition('.')

        arch_name = archive_name[0]

        source = "/tmp/{}".format(archive_path)

        destination = "/data/web_static/releases/".format(arch_name)

        run("tar -xvf {} -C {}".format(source, destination))

        run("rm {}".format(archive_path))
        run("unlink /data/web_static/current")
        run("link -s {} /data/web_static/current".format(destination))
    except Exception:
        return False

    return True


if __name__ == "__main__":
    do_deploy()
