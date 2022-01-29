#!/usr/bin/env python3
import subprocess

from psysinfo_func import disk_func

subprocess.call(['ls','-l', '/tmp/'])
disk_func()
