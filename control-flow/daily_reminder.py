# daily_reminder.py
# Prompt for a single task
task = input("Enter your task: ")

# Use a loop to ensure valid priority input
while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ["high", "medium", "low"]:
        break
    else:
        print("Invalid input. Please enter high, medium, or low.")

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Reminder: '{task}' has an unknown priority"

# Modify reminder if time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif priority == "low":
    reminder += ". Consider completing it when you have free time."

# Provide customized reminder
print(reminder)
