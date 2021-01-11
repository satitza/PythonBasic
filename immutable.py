def immutable_demo():
    n = 5
    print('id(n) = 0x{}, n value is {}'.format(id(n), n))
    n = n + 4
    print('id(n) = 0x{}, n value is {}'.format(id(n), n))


def mutable_demo():
    list = ['Anonymous']
    print('id(n) = 0x{}, list value is {}'.format(id(list), list))
    list[0] = 'Anonymous Hacker'
    print('id(n) = 0x{}, list value is {}'.format(id(list), list))

    list2 = list
    list2[0] = 'Anonymous Hacker 2'

    print('id(n) = 0x{}, list value is {}'.format(id(list), list))
    print('id(n) = 0x{}, list2 value is {}'.format(id(list2), list2))


immutable_demo()
print('#####################################')
mutable_demo()

_ = 'WTF for what'
print(_)
print('0x{}'.format(id(_)))
print(type(_))
