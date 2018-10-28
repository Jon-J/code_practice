with open("test.txt") as fd:
    line = fd.readline()
    while line:
        print(line)
        line = fd.readline()
        print("something = ", line)
        if fd.tell() == eof:
            print("tell - ", fd.tell())
