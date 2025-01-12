from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date and time
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Prompts the user to input a number of days and calculates the future date.
    """
    try:
        # Prompt the user for the number of days to add
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        
        # Calculate the future date
        current_date = datetime.now()  # Get the current date
        future_date = current_date + timedelta(days=days_to_add)  # Add days
        formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format the future date
        
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

def main():
    """
    Main function to execute the datetime operations.
    """
    display_current_datetime()  # Show the current date and time
    calculate_future_date()  # Calculate a future date

if __name__ == "__main__":
    main()
