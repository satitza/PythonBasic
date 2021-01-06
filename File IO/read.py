def openFile(fileName):
    return open(fileName, "r+")


if __name__ == "__main__":
    file = openFile('test.txt')
    print(file.read())
    print(file.buffer)
    print(file.mode)
    print(file.encoding)
