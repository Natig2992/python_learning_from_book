#!/usr/bin/env bash


function uname_func ()
{
    UNAME="uname -a"

    printf "\n"
    printf "Gathering system info with '$UNAME' command\n:"
    $UNAME
}

function disk_func ()
{ 
    DISKSPACE="df -h"

    printf "\n"
    printf "Gathering diskspace information with '$DISKSPACE' command:\n" 
    $DISKSPACE
}

function memory_info ()
{

    MEM_INFO="free -m"
    printf "\n"
    printf "Gathering memory info with '$MEM_INFO' command:\n" 
    $MEM_INFO
}


# Main function, calling other two functions:

function main () 
{
    uname_func
    disk_func
    memory_info
}

main
