#!/usr/bin/env bash


function uname_func ()
{
    UNAME="uname -a"

    printf "\n"
    printf "Gathering system info with  %s command:\n\n" 
    $UNAME
}

function disk_func ()
{ 
    DISKSPACE="df -h"

    printf "\n"
    printf "Gathering diskspace information with %s command:\n\n" 
    $DISKSPACE
}

# Main function, calling other two functions:

function main () 
{
    uname_func
    disk_func
}

main
