import os
import shutil
from os import path
from shutil import make_archive
from zipfile import ZipFile


if path.exists("textfile.txt"):
    src = path.realpath("textfile.txt")

    # head, tail = path.split(src)
    # print("path:", head)
    # print("file:", tail)

    # dst = src + ".bak"
    # shutil.copy(src, dst)

    # os.rename("newfile.txt", "textfile.txt")

    # root_dir,tail = path.split(src)
    # shutil.make_archive("archive", "zip", root_dir)

    with ZipFile("test.zip", "w") as newzip:
        newzip.write("textfile.txt")
        newzip.write("textfile.txt.bak")
