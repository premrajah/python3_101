#
# File system shell methods
#
import os
from os import path
import shutil # shell util
from shutil import make_archive
from zipfile import ZipFile

def main():
    # make a duplicate of existing file
    if path.exists("textfile.txt"):
        ## get the path to the file in the current directory
        src = path.realpath("textfile.txt")

        ## make a backup copy by appening 'bak' to the name
        dst = src + ".bak"

        ## copy over the permissions, modification times and other info
        # shutil.copy(src, dst)
        # shutil.copystat(src, dst)

        ## rename the original file
        # os.rename("textfile.txt", "newfile.txt")

        ## putting things into a zip archive
        # root_dir, tail = path.split(src)
        # shutil.make_archive("archive", "zip", root_dir)

        ## more fine-grained control over ZIP files
        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("textfile.txt")
            newzip.write("textfile.txt.bak")



        print("...done.")


if __name__ == "__main__":
    main()