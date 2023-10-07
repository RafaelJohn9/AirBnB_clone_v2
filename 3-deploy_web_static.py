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

# archiving contents
archive = do_pack()


@task
def deploy():
    """
    the function used in automation
    """
    global archive

    if archive is None:
        return False
    archive = str(archive)

    return (do_deploy(archive))
