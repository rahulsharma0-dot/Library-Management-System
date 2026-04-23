from datetime import datetime
from utils import books, issued_books

def issue():
    book_name = input(" Enter Book Name: ").upper()

    if book_name in books and books[book_name]["available"]:
        student = input(" Enter Student Name: ")
        days = int(input(" Enter number of days: "))

        issued_books[book_name] = {
            "student": student,
            "issue_date": datetime.now().date(),
            "days": days
        }

        books[book_name]["available"] = False

        print(f"\n Book issued to {student}")
        print(" Fine Policy:")
        print("1st week: ₹10/day")
        print("2nd week: ₹20/day")
        print("3rd week: ₹30/day ...")

    else:
        print(" Book not available")