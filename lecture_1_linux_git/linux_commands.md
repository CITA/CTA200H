# Linux Commands

Here is a cheatsheet with some of the commands you may find useful throughout the course and your research work.

## Basic Commands

    man     manual of commands and certain functions

    ls      list directory content
    ls -l   list and show info about the directory
    ls -ld  list directory entries instead of contents
    ls -a   show hidden directory
    ls -la

    cd      change directory
    pushd   create a stack of directories, change to next dir on stack
    popd    deleted current director from stack, change to next dif
    pwd     print working directory

    cp      copy file or directory
    cp -a   copy directory
    mv      move, i.e., rename, file or directory
    rmdir   remove directory
    rm      remove files
    rm -rf  forcefully remove directory and/or files including subdirectories

    chmod   change permissions (who can read/write/execute) on files or directories

    history print the last few commands; history -n prints the last n
    echo    print arguments, e.g., `echo $0' prints the type of shell you are running
    whoami  your login identity; same as `echo $USER'

    cat     concatenate. print file contents to screen
    less    show content, allowing for "up/down" movement

    which   find out the location of a given command program

## Directory Symbols

    /       root directory of file-system
    ~       home directory of current user, same as /home/$USER
    .       current directory
    ..      parent directory


## Remote Access and Remote File Transfer

    ssh USERNAME@SERVER.cita.utoronto.ca    login to remote computer ("SERVER")
    scp SOURCE TARGET                       secure copy a file from one computer to another
    rsync -avP SOURCE TARGET                like scp, but retaining metadata 
