
## Create a python program that pretty prints the PATH environment variable.

## environment variable -> a dynamic-named value that can affect the way
## running processes will behave on a computer

## Programs and other executable files can be in many directories, so operating
## systems provide a search path that lists the directories that the OS searches
## for executables.

## The path is stored in an environment variable, which is a named string
## maintained by the operating system. This varialbe contains information
## available to the command shell and other programs.

## PATH is an environment variable on Unix-like operating systems, DOS, OS/2,
## and Microsoft Windows, specifying a set of directions where executable
## programs are located. In general, each executing process or user session
## has its own PATH setting.

import os
import pprint

PATH = os.environ['PATH']
PATH_list = PATH.split(';')
pprint.pprint(PATH_list)
