from dbConfig import DATABASE
from entity import Staff


def get_staffs():
    staffs = [
        Staff(**data) for data in DATABASE.get("staff", [])
    ]

    return staffs
