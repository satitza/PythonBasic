def _private_method():
    print('Private method')


_private_var = 'private var'


class SupperClass(object):
    static_number_supper_class = 100

    def __init__(self):
        print('This constructor of supper')

    def methodForImplement(self):
        raise NotImplementedError('The subclass must implement this method')

    @property
    def passMethod(self):
        pass

    def __str__(self):
        if __name__ != '__main__':
            return __name__
        else:
            return 'This __str__ method from supper class'
