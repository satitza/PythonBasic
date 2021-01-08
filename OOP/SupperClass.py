class SupperClass(object):

    def __init__(self):
        print('This is constructor  of supper class ')

    def method1SP(self):
        print('method 1 of supper class')


class SubClass(SupperClass):
    def __init__(self):
        SupperClass.__init__(self)
        print('This is constructor  of sub class ')

    def method1SB(self):
        print('method 1 of supper class')


if __name__ == "__main__":
    sp = SupperClass()
    sc = SubClass()
    sc2 = SubClass()

    print(hex(id(sp)))
    print(hex(id(sc)))
    print(hex(id(sc2)))
    print(hex(id(sc2.method1SB())))

