from Package1 import *
from Package2 import *


class SubClass(SupperClass):
    static_number_supper_class = 150
    static_number_sub_class = 200

    def __init__(self):
        SupperClass.__init__(self)
        self.name = 'Sub class name variable'

    @property
    def methodForImplement(self):
        print('Method of supper class has implemented')

    def __str__(self):
        if __name__ != '__main__':
            return __name__
        else:
            return 'This __str__ method from sub class'


class MyClass(object):

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    # def __str__(self):
    #    return 'This __str__ method from  MyClass'

    @property
    def getClassName(self):
        return self.__class__.__name__

    def __repr__(self):
        return repr(self.name)


if __name__ == '__main__':
    print(f'Python OOP and Modules  {__name__}')

    c = ClassInP1Modules1()
    c.methodInClassInP1Modules1()

    P1Modules2Function1()
    print(_private_var)

    ###########################################################

    sub = SubClass()

    print(sub)
    print(SubClass.static_number_supper_class)
    print(SubClass.static_number_sub_class)
    print(sub.name)

    sup = SupperClass()

    ############################################################

    # sub_list = [
    #    SubClass(),
    #    SubClass(),
    #    SubClass(),
    #    sub
    # ]

    # for i in sub_list:
    #    print(i)

    sub.methodForImplement
    sub.passMethod  # This is decorator properties method from supper class

    m = MyClass('My Class', 'Description for my class')
    print(m)
    print(m.getClassName)

    attr = vars(m)
    for k, v in attr.items():
        print(f'Key : {k}, Value : {v}')


else:
    pass
