#!/usr/bin/python3
"""a Fabric script  that creates"""
from fabric.api import *
from time import strftime
from datetime import datetime
import os
from os import path


env.hosts = ['35.175.126.161', '54.164.52.24']


def do_pack():
    """creating a tar file"""
    try:
        now = datetime.now()
        local("mkdir -p versions/")
        time_format = now.strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_" + time_format + ".tgz"
        archive_path = os.path.join("versions", archive_name)
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception as e:
        return None


def do_deploy(archive_path):
    """deploys the archives to server"""
    try:
        print("Starting do_deploy function...")
        if not (path.exists(archive_path)):
            return False

        # uploading the archive
        put(archive_path, "/tmp/")

        # uncompress the archive
        parts = archive_path.split('_')
        time_stamp = parts[2].split(".")[0]
        run("sudo rm -rf /data/web_static/releases/\
web_static_{}".format(time_stamp))
        run("sudo mkdir -p /data/web_static/releases/\
web_static_{}".format(time_stamp))
        run("sudo tar -xzf /tmp/web_static_{}.tgz -C /data/\
web_static/releases/web_static_{}".format(time_stamp, time_stamp))

        # delete the archive from web_server
        run("sudo rm -rf /tmp/web_static_{}.tgz".format(time_stamp))

        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(time_stamp, time_stamp))

        # delete the file
        run("sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static".format(time_stamp))
        # delete the symbolic link
        run("sudo rm -rf /data/web_static/current")

        # create a new symblolic link
        run("sudo ln -sf /data/web_static/releases/\
web_static_{} /data/web_static/current".format(time_stamp))

        return True
    except Exception as e:
        return False


def deploy():
    """Deploy a new version to the server"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)


def do_clean(number=0):
    """fabric method"""
    number = int(number)
    if number == 0:
        number = 1
    local("cd versions && ls -t | head -n -{} | xargs rm -rf".format(number))
    path = "/data/web_static/releases"
    run("cd {} ; ls -t | head -n -{} | xargs rm -fr".format(path, number))
