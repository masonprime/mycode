#!/usr/bin/env python3

import shutil

import os

os.chdir("/home/student/mycode/")

# create a file is it doesn't already exist

shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# create a directory if it doesn't already exist

shutil.copytree("5g_research/", "5g_research_backup/")

