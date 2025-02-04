import pytest
from project import Personal_Library

@pytest.fixture

def setup_library():
    return Personal_Library

def test_add_book(setup_library):
    project = setup_library
    project.add_book("The Lord of the Rings", "J.R.R Tolkien")
    assert len(project.books) == 1
    assert project.books[0]["title"] == "The Lord of the Rings"

def test_remove_book(setup_library):
    project = setup_library
    project.add_book("Foundation", "Isaac Asimov")
    project.remove_book("Foundation")
    assert  len(project.books) == 0

def test_list_books(setup_library):
    project = setup_library
    project.add_book("Call of Cthulhu", "H.P Lovecraft")
    project.add_book("The final empire", "Brandon Sanderson")
    assert len(project.books) == 2


