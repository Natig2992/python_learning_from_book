#!/usr/bin/env python3
import subprocess

def uname_func():
    uname = "uname"
    uname_arg = "-a"
    print()
    print ("Gathering system information with %s command:\n" % uname)
    subprocess.call([uname, uname_arg])

def disk_func():
    diskspace = "df"
    diskspace_arg = "-h"
    print()
    print ("Gathering diskspace information with %s command:\n" % diskspace)
    subprocess.call([diskspace, diskspace_arg])

# Main function, calling other two functions:

def main():
    uname_func()
    disk_func()
main()
