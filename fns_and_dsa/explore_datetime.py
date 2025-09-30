from datetime import datetime, timedelta

def display_current_datetime():
    # Save current date and time
    current_date = datetime.now()
    # Print in YYYY-MM-DD HH:MM:SS format
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(days_to_add):
    # Get today's date
    today = datetime.now()
    # Calculate future date
    future_date = today + timedelta(days=days_to_add)
    # Print in YYYY-MM-DD format
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

def main():
    # Part 1: Display current datetime
    display_current_datetime()
    
    # Part 2: Ask user for days and calculate future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    main()
