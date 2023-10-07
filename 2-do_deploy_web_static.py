#!/usr/bin/python3

"""
a fabric script (based on 1-pack_web_static.py)
that distributes an archive to your web servers
using the function do_deploy
"""
from fabric.api import *
from os import path
import sys

# sets the list of web server ip addresses
env.hosts = ['100.25.109.79', '18.206.207.45']


@task
def do_deploy(archive_path):
    """
    a fabric script that distributes an archive to your web servers
    """
    try:
        if not path.exists(archive_path):
            return False
        remote_dest = "/tmp"

        # breaking down archive_path name
        dirBreak = archive_path.split("/")

        # dirBreak[-1] contains name of the file
        extBreak = dirBreak[-1].split(".")
        name = extBreak[0]

        cmd1 = f"sudo tar -xzf {remote_dest}/{dirBreak[-1]}\
                -C /data/web_static/releases/{name} --strip-components 1"

        put(local_path=archive_path, remote_path=remote_dest)
        run(f'mkdir -p /data/web_static/releases/{name}')
        run(cmd1)
        run(f'rm -rf {remote_dest}/{dirBreak[-1]}')

        # symbolic link
        run("sudo rm -rf /data/web_static/current")
        run(f'ln -fs /data/web_static/releases/{name}\
                /data/web_static/current')
        return True
    except Exception:
        return False 
