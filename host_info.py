#!/usr/bin/env python3

# Get most important info about the current Linux host.
#
#


import os
import platform

# def linux_distribution():
#     print(platform.linux_distribution())

def os_version():
    print(os.major())

os_version()

linux_distribution()