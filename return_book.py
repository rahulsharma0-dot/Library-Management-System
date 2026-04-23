from utils import books, issued_books, calculate_fine

def return_book():
    book_name = input(" Enter Book Name: ").upper()

    if book_name in issued_books:
        record = issued_books[book_name]

        fine = calculate_fine(record["issue_date"], record["days"])

        print(f"\n Student: {record['student']}")

        if fine > 0:
            print(f" Fine: ₹{fine}")
        else:
            print(" No fine!")

        books[book_name]["available"] = True
        del issued_books[book_name]

        print(" Book returned successfully!")

    else:
        print(" Book not issued")