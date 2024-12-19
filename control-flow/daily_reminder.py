# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Generate reminder based on priority and time sensitivity using match-case and if statement
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Consider addressing it soon."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
        if time_bound == "yes":
            reminder += " Make sure to complete it today."
        else:
            reminder += " You can work on it when you have some time."
    case "low":
        reminder = f"'{task}' is a low priority task."
        if time_bound == "yes":
            reminder += " It would be great to finish today, but it's not urgent."
        else:
            reminder += " Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority level entered. Please enter high, medium, or low."

# Output the final reminder
print("Reminder:", reminder)
