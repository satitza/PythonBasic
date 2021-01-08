def openFile(fileName, mode):
    return open(fileName, mode)


if __name__ == "__main__":
    try:
        file = openFile('test.txt', 'r+')
        print(file.read())
        print(file.buffer)
        print(file.mode)
        print(file.encoding)
    finally:
        file.close()

    with openFile('test.txt', 'r+') as file:
        print(file.read())
