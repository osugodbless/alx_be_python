# Collect user inputs
task = input("Enter your task description: ")
priority = input("What is the task priority level? (high, medium, low): ").lower()
time_bound = input("Is the task time bound? (yes/no): ").lower()

# 
match priority:
    case level if level == "high" and time_bound == "yes":
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case level if level == "high" and time_bound == "no":
        print(f"Reminder: '{task}' is a high priority task. Tackle it immediately after completing all time-conscious, high priority task!")
    case level if level == "medium" and time_bound == "yes":
        print(f"Reminder: '{task}' is a medium priority task that should be tackled today after completing all high priority task!")
    case level if level == "medium" and time_bound == "no":
        print(f"Reminder: '{task}' is a medium priority task. Tackle it immediately after completing all time-conscious, medium priority task!")
    case level if level == "low" and time_bound == "yes":
        print(f"Reminder: '{task}' is a low priority task that requires immediate attention. Consider delegating it to someone and focus on tasks with higher priority")
    case level if level == "low" and time_bound == "no":
        print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time. You might also wanna consider delegating it to free more time for rest") 
    case _:
        if time_bound != "yes" and time_bound != "no":
            print("Please enter 'yes' or 'no' for time bound")
        else:
            print("You entered an invalid priority level. Please enter any of the options (high/medium/low)")
