class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __eq__(self, other):
        if other is None or other.id is None:
            return False
        return self.id == other.id


if __name__ == "__main__":
    user1 = User(1, 'Anonymous', 'Hacker')
    user2 = User(1, 'Anonymous', 'Hacker')

    print(user1 == user2)
    print(id(user1), id(user2))
