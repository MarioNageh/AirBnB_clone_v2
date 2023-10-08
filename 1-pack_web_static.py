#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the"""
from fabric.api import local, task
from datetime import datetime


@task
def do_pack():
    """Function To Compress File Using tar"""
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M")
        folder_to_save = "versions"
        local(f"mkdir -p {folder_to_save}")
        file_name_generated = f"web_static_{current_time}.tgz"
        local(f"tar -cvzf {folder_to_save}/{file_name_generated} web_static")
        return f"{folder_to_save}/{file_name_generated}"
    except Exception as e:
        return None
