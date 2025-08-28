import sys


def custom_generator(limit):
    for i in range(limit):
        yield i


if __name__ == "__main__":
    print('Custom generator')

    print(custom_generator(50000))
    print(sys.getsizeof(custom_generator(50000)))

    for i in custom_generator(50000):
       print(i)
