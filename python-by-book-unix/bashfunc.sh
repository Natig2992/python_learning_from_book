#!/usr/bin/env bash

function shfunc(){
    printf "Hello Wolrd!\n"
}

for ((i=0; i <= 8 ; i++))
do
    shfunc
done
