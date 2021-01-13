print(f'This is Modules 1 in Package 1 full name of modules is {__name__}')


class ClassInP1Modules1:
    def __init__(self):
        print('This is constructor is ClassInP1Modules1')

    @classmethod
    def methodInClassInP1Modules1(cls):
        print('This is method methodInClassInP1Modules1')
