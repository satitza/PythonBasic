import sys


def outerFunction():
    print('Outer method')

    def innerFunction1():
        print('Inner function 1')

    def innerFunction2():
        print('Inner function 2')

    innerFunction1()
    innerFunction2()


if __name__ == "__main__":
    print('main method')
    outerFunction()

    arr = [1, 2, 3, 4, 5, 6]
    print(sys.path)
