"""
This module implements logic to obtain current date and time and also calculates a future
date and time using Python's datetime module
"""
from datetime import datetime, timedelta

def display_current_datetime():
    """
    This function finds the current date and time and formats it to a the Year-Month-Day
    Hour-Minute-Second format using the strftime method and returns the formatted date
    as a string
    """
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: ", current_date)
    return current_date

def calculate_future_date():
    """
    This function asks the user to enter a number of days and adds those days to the
    current date returned by the display_current_datetime function, and returns the
    resulting date in the format of Year-Month-Date
    """
    current_date = display_current_datetime()
    current_date_as_datetime_obj = datetime.strptime(current_date, '%Y-%m-%d %H:%M:%S')
    num_of_days = int(input("Enter the number of days to add to the current date: "))
    future_days = timedelta(days=num_of_days)

    future_date = current_date_as_datetime_obj + future_days

    future_date = future_date.strftime("%Y-%m-%d")
    print("Future date:", future_date)

if __name__ == "__main__":
    calculate_future_date()
