from datetime import datetime

books = {}
issued_books = {}

def calculate_fine(issue_date, allowed_days):
    today = datetime.now().date()
    days_passed = (today - issue_date).days

    if days_passed <= allowed_days:
        return 0

    late_days = days_passed - allowed_days
    fine = 0

    for day in range(1, late_days + 1):
        week = (day - 1) // 7 + 1
        fine += 10 * week

    return fine