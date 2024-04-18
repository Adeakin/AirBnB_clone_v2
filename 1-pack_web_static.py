#!/usr/bin/python3
# Create a .tgz archive from the web_static directory.
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Generate a compressed archive of web_static."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if not os.path.isdir("versions") and local("mkdir -p versions").failed:
        return None
    if local("tar -cvzf {} web_static".format(file)).failed:
        return None
    return file
