# Linux Commands

Here is a cheatsheet with some of the commands you may find useful throughout the course and your research work.

## Basic Commands

    man     manual of commands and certain functions

    ls      list directory content
    ls -l   list and show info about the directory
    ls -ld    list directory entries instead of contents
    ls -a   show hidden directory
    ls -la

    cd      change directory
    pwd     print working directory

    cp      copy file or directory
    cp -a   copy directory
    mv      move, rename file or directory
    rmdir   remove directory
    rm      remove files
    rm -rf    forcefully remove directory and/or files including subdirectories

    cat     concatenate. print file contents to screen
    less    show content, allowing for "up/down" movement

    which   find out the location of a given command program

## Directory Symbols

    /       root directory of file-system
    ~       home directory of current user, same as /home/$USER
    .       current directory
    ..      parent directory


## Remote Access and Remote File Transfer

    ssh USERNAME@SERVER.cita.utoronto.ca
    scp SOURCE TARGE
    rsync -avP SOURCE TARGET