def daily_reminder():
    # Prompt for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process the task based on priority and time sensitivity using Match Case
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = f"'{task}' has an unknown priority"

    # Modify the reminder based on time sensitivity
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += "."

    # Print the customized reminder
    print("Reminder:", reminder)

# Example usage of the function
daily_reminder()
