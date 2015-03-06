# Bad programming practices?
import os
from os import path
import datetime
from datetime import date
from datetime import time
from datetime import timedelta


def main():
    print(os.name)

    # print("Item exists:", str(path.exists("textfile.txt")))
    # print("Item is a file:", str(path.isfile("textfile.txt")))
    # print("Item is a directory:", str(path.isdir("textfile.txt")))

    # print("Items path:", str(path.realpath("textfile.txt")))
    # print("Items path and name:", str(path.split("textfile.txt")))

    # t = time.ctime(path.getmtime("textfile.txt"))
    # print(t)
    # print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

    # td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    # print("It has been", str(td), "the file was modified")
    # print("0r,", str(td.total_seconds(), "seconds"))


if __name__ == "__main__":
    main()
