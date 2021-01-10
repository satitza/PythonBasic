from Package1.P1Modules2 import P1Modules2Function1
from Package1.P1Modules1 import ClassInP1Modules1
from Package2.Class_Inheritance import SupperClass


class SubClass(SupperClass):
    def __init__(self):
        SupperClass.__init__(self)

    def methodForImplement(self):
        print('Method of supper class has implemented')


if __name__ == '__main__':
    print('Python OOP and Modules')

    c = ClassInP1Modules1()
    c.methodInClassInP1Modules1()

    P1Modules2Function1()

    ###########################################################

    sub = SubClass()
    sub.methodForImplement()
