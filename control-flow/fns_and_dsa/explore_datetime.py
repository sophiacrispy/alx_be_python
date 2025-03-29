
from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    
    current_datetime = datetime.now()
    
    
    current_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    
    
    print(f"Current date and time: {current_date}")

def calculate_future_date():
    """
    Prompts the user to enter a number of days and calculates the future date.
    """
    
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    
    current_datetime = datetime.now()
    
    
    future_date = current_datetime + timedelta(days=days_to_add)
    
    
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    
    
    print(f"Future date: {formatted_future_date}")


def main():
    display_current_datetime()
    calculate_future_date()


if __name__ == "__main__":
    main()
