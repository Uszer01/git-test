#!/bin/bash

function get_size() {
    if [[ -d "$1" ]] ; then
        echo $(du -sh $1 | cut -f1)
    else
        echo $(stat -c '%s' $1)
    fi
}

function analyze_directory() {
    for file in * ; do
        size=$(get_size $file)
        printf "%s\t%s\n" $file $size
    done
    
    for dir in * ; do
        if [[ -d $dir ]] ; then
            pushd $dir > /dev/null
            analyze_directory
            popd > /dev/null
        fi
    done
}

analyze_directory | sort -nrk2
