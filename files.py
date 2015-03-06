def main():
    # f = open("textfile.txt", "w+")
    # for i in range(10):
    #     f.write("This is line %d\n" % (i+1))

    # f.close()

    f = open("textfile.txt", "r")
    # contents = f.read()
    # print(contents)

    fl = f.readlines()
    for x in fl:
        print(x)


if __name__ == "__main__":
    main()

