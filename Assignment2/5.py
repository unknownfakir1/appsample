'''
Write a function that takes the path of a directory and prints
out the paths files within that directory as well as
 any files present in the nested directories. (This function is similar to os.walk. Please don't use
os.walk in your answer. We are interested in your ability to work with nested structures)
'''

import os


def fold(path):
    dir_list = os.listdir(path)

    print("Files and directories in '", path, "' :")

    # prints all files
    fs = [f for f in dir_list if os.path.isfile(os.path.join(path, f))]
    print(*fs, sep="\n")


def listdirs(rootdir):
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            fold(d)
            listdirs(d)


rootdir = r'C:\Users\Rajnandini.K\Desktop'
listdirs(rootdir)
