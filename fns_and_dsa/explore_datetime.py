from datetime import datetime, timedelta

# Display the current date and time
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)

# Calculate a future date
def calculate_future_date():
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Future date:", formatted_future_date)

display_current_datetime()
calculate_future_date()
    
