from configurationHelper import __config__
from service import BookService, MemberService, StaffService, LibraryService
from repository import get_staffs


staffs = get_staffs()
print(staffs)

def setup():
    # region Initiate Services
    bookService = BookService()
    memberservice = MemberService()
    staffService = StaffService()
    libraryService = LibraryService()
    # endregion
    return bookService, memberservice, staffService, libraryService


def run():
    pass


def main():
    bookService, memberservice, staffService, libraryService = setup()

    run(bookService, memberservice, staffService, libraryService)

input()