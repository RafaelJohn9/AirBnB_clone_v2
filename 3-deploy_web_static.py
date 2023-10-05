#!/usr/bin/python3
"""
a fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distrbutes an archive to
your web servers using the function deploy
"""

from fabric.api import *
from os import path
from datetime import datetime

# imports
module_name_1 = '1-pack_web_static'
module_1 = __import__(module_name_1)
do_pack = module_1.do_pack

# file imports
module_name_2 = '2-do_deploy_web_static'
module_2 = __import__(module_name_2)
do_deploy = module_2.do_deploy

# set the list of web server ip addresses
env.hosts = ['18.206.207.45', '100.25.109.79']


@task
def deploy():
    """
    the function used in automation
    """
    archive = do_pack()
    if archive == None:
        return False

    return (do_deploy(archive))
