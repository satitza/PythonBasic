class User(object):
    count_user = 0

    def __init__(self, username, password):
        self.username = username
        self.password = password
        User.count_user += 1

    def getUsernameAndPassword(self):
        return self.username + ' / ' + self.password

    @property
    def getUsernameAndPassword(self):
        return self.username + ' / ' + self.password

    def __del__(self):
        print('Object was destroyed ... ')


def add(a, b):
    return a + b


if __name__ == "__main__":
    user1 = User('user1', 'password1')
    user2 = User('user2', 'password2')

    print(user1.getUsernameAndPassword)
    print(User.count_user)

    print(type(add))
    print(dir(add))
