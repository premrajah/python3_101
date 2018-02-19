#
# Comments go here
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    # code goes here
    print("--OS Path--")
    print("OS Name: ", os.name)

    # check existance of file
    print("Item exists: " + str(path.exists("textfile.txt")))
    print("Item is a file: " + str(path.isfile("textfile.txt")))
    print("Item is a dir: " + str(path.isdir("textfile.txt")))

    # work with full path
    print("Item real path: " + str(path.realpath("textfile.txt")))
    print("Item path and name: " + str(path.split(path.realpath("textfile.txt"))))

    ## get modification time
    t = time.ctime(path.getmtime("textfile.txt"))
    print("Modified time: " + t)
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

    # calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(
        path.getmtime("textfile.txt")
    )
    print("It has been " + str(td) + " since last file modified.")
    print("or " + str(td.total_seconds()) + " seconds")
    


if __name__ == "__main__":
    main()