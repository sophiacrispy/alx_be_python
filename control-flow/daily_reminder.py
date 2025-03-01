
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()


def generate_reminder(task, priority, time_bound):
    
    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a high priority task"
            if time_bound == "yes":
                reminder += " that requires immediate attention today!"
            else:
                reminder += ". Please complete it as soon as possible."
        case "medium":
            reminder = f"Reminder: '{task}' is a medium priority task"
            if time_bound == "yes":
                reminder += " and should be completed soon!"
            else:
                reminder += ". Complete it when you get a chance."
        case "low":
            reminder = f"Reminder: '{task}' is a low priority task"
            if time_bound == "yes":
                reminder += " but can be done at a more convenient time."
            else:
                reminder += ". Consider completing it when you have free time."
        case _:
            reminder = "Invalid priority entered. Please enter 'high', 'medium', or 'low'."
    
    
    print(reminder)

generate_reminder(task, priority, time_bound)
