#!/usr/bin/python3

"""
a fabric script that generates a .tgz archive from the contents of 
the web_static folder of the airbnb clonge repo using the funcion do_pack
"""
from fabric import task
from datetime import datetime
import os

@task
def do_pack():
    """
    the fuctions used in archiving
    """
    if not os.path.exists('versions'):
        local('mkdir -p versions')

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    source = "./web_static"
    archiveName = f"web_static_{timestamp}.tgz"

    result = local(f"tar -cvzf versions/{archiveName} {source}")
    
    if result.failed:
        return None
    else:
        return f"versions/{archiveName}"
