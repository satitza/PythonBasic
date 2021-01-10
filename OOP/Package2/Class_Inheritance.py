class SupperClass(object):

    def __init__(self):
        print('This constructor of supper class')

    def methodForImplement(self):
        raise NotImplementedError('The subclass must implement this method')
