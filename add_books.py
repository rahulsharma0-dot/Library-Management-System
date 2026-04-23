from utils import books

def add():
    book_name = input(" Enter Book Name: ").upper()

    if book_name in books:
        print(" Book already exists!")
    else:
        books[book_name] = {"available": True}
        print(" Book added successfully!")