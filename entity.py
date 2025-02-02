class Book:
    def __init__(self, id, name, author, edition, genre):
        self.id = id
        self.name = name
        self.author = author
        self.edition = edition
        self.genre = genre
        self.member = None
        self.durationAlloted = None
        self.dateTimeAlloted = None
        self.staffId = None


class Member:
    def __init__(self, id, name, durationOfMembership, dateTimeOfMembership, staffId):
        self.id = id
        self.name = name
        self.books = []
        self.durationOfMembership = durationOfMembership
        self.dateTimeOfMembership = dateTimeOfMembership
        self.staffId = staffId


class Staff:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []


class Staff: 
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    def __str__(self):  # it is called when str(object) is called
        return f"<Staff- id: `{self.id}`, name: `{self.name}`>"

    def __repr__(self):  # it is called representation method, which called for any kind of representation of the object
        return f"<Staff- id: `{self.id}`, name: `{self.name}`>"
