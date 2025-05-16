import datetime

def validate_date(date_text):
    """Ensure the date is in YYYY-MM-DD format."""
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def input_float(prompt):
    """Safely get a float input from user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def input_date(prompt):
    """Safely get a valid date input from user."""
    while True:
        date = input(prompt)
        if validate_date(date):
            return date
        else:
            print("Invalid date format. Use YYYY-MM-DD.")

def currency_format(amount):
    """Format a float as currency."""
    return f"${amount:,.2f}"
