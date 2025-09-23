"""
This module uses loops, conditional statements, and Match case to create a reminder
notification based on priority level and whether the task is time-bound

The pseudocode is as follows:
    1. Ask the user to enter the task and save it in a variable
    2. Ask the user to enter the task's priority level (high, medium, low)
    3. Ask the user whether the task is time bound.
    4. Process the task in the following manner:
        - If the task priority is high, check that:
            -> if it is timebound, then it has the highest priority and
               as such, you return the a customized reminder.
            -> if it isn't time bound, then it has the 2nd highest priority
               and as such, return an appropriate customized reminder.
        - If the task's priority is medium, check that:
            -> if it's timebound, then it has the 3rd highest priority and
               as such, return an appropriate customized reminder
            -> if it's not timebound, them it has the 4th highest priority
               and as such, return an appropriate customized reminder
        - If the task's priority is low, check that:
            -> If it's timebound, then it has the 5th highest priority and
               as such, return an appropriate customized reminder
            -> If it's not timebound, then it has the 6th highest priority
               and as such, return an appropriate customized reminder
    5. The reminders are as follows:
        - For timebound tasks, the reminder is:
            f'{task} is a {priority_level} task that requires immediate attention'
        - For non-timebound tasks, the reminder is:
            f'{task} is a {priority_level} task. Consider completing it when you
              have free time'
"""

def daily_reminder():
    user_task = str(input("Enter your task: ")).strip()
    priority = str(input("Priority (high/medium/low): ")).strip().lower()
    time_bound = str(input("Is it time-bound? (yes/no): ")).strip().lower()

    match priority:
        case "high":
            if time_bound == "yes":
                reminder = f"'{user_task}' is a high priority task that requires immediate attention today!"
                print(f"Reminder: {reminder}")
            else:
                reminder = f"'{user_task}' is a high priority task. Consider completing as soon as possible."
                print(f"Reminder: {reminder}")
        case "medium":
            if time_bound == "yes":
                reminder = f"'{user_task}' is a medium priority task that requires some attention today!"
                print(f"Reminder: {reminder}")
            else:
                reminder = f"'{user_task}' is a medium priority task. Consider completing it soon."
                print(f"Reminder: {reminder}")
        case "low":
            if time_bound == "yes":
                reminder = f"'{user_task}' is a low priority task. Consider completing it soon"
                print(f"Note: {reminder}")
            else:
                reminder = f"'{user_task}' is a low priority task. Consider completing it when you have free time."
                print(f"Note: {reminder}")
        case _:
            reminder = "Sorry. Please make sure you enter valid program parameters specified in the prompts"

if __name__ == "__main__":
    daily_reminder()
