def openFile(fileName):
    return open(fileName, "rb+")


if __name__ == "__main__":

    try:
        with openFile('Intel_X86.pdf') as file:
            file_data = file.read()
    except Exception as ex:
        print(ex)
    finally:
        print('Success for open file.')
