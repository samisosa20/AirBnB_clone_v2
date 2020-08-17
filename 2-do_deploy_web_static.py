#!/usr/bin/python3
from fabric.api import local, put, run, env
from datetime import datetime
import os

env.hosts = ['142.44.167.228', '35.229.95.227']
env.user = 'ubuntu'


def do_pack():
    """enerates a .tgz archive from the contents of the web_static folder
    of AirBnB clone.
    All archives must be stored in the folder versions
    (folder will be created if it doesn’t exist).
    Return: Archive path if the archive has been successfully generated.
    Otherwise, it should return None
    """
    try:
        if not os.path.exists("./versions"):
            local("mkdir versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "web_static_" + date + ".tgz"
        command = "tar -cvzf " + "./versions/" + file_name + " ./web_static"
        local(command)
        return "versions/" + file_name
    except:
        return None

def do_deploy(archive_path):
    """Write a Fabric script that generates a .tgz archive from the contents 
    of the web_static folder of your AirBnB Clone repo, using the function do_pack.
    Args:
        archive_path (string): archive from the contents of the web_static

    Returns:
        bool: false or true
    """
    if not os.path.exists(archive_path):
        return False
    try:
        list_aux1 = archive_path.split(".tgz")
        archive_wo_ext = "".join(list_aux1)
        list_aux2 = archive_wo_ext.split("versions/")
        archive_wo_ext_ver = "".join(list_aux2)
        list_aux3 = archive_path.split("versions/")
        archive_wo_ver = "".join(list_aux3)
        put(archive_path, '/tmp/')
        run("mkdir -p /data/web_static/releases/{}/".
            format(archive_wo_ext_ver))
        run("tar -zxf /tmp/{} -C /data/web_static/releases/{}/"
            .format(archive_wo_ver, archive_wo_ext_ver))
        run("rm -rf /tmp/{}".format(archive_wo_ver))
        run("mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}/".format(archive_wo_ext_ver,
                                                archive_wo_ext_ver))
        run("rm -rf /data/web_static/releases/{}/web_static".
            format(archive_wo_ext_ver))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
            format(archive_wo_ext_ver))
        print("New version deployed!")
        return True
    except:
        return False
