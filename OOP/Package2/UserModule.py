class User(object):

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    def __eq__(self, other) -> bool:
        return self.__id == other.__id

    def __hash__(self) -> int:
        return super().__hash__(self.id)
