from utils import books

def show():
    print("\n AVAILABLE BOOKS:\n")

    available = False
    for book, details in books.items():
        if details["available"]:
            print(f" {book}")
            available = True

    if not available:
        print(" No books available")