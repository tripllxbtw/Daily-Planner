#planning for the future
tasks = {
    "09:00": "Breakfast",
    "11:30": "Meeting with team"
}


while True:
    choice = input("Would you want to choice a 'add' or 'remove' or 'show' or 'exit' a task? :").lower().strip().upper()
    choice = choice.lower()  # Normalize input to lowercase for consistency
    tasks = tasks  # Ensure tasks is defined in the loop scope
    if choice == "add":
        time = input("Enter the time for the task (HH:MM): ")
        tasks[time] = input("Enter the task description: ")
    elif choice == "remove":
        time = input("Enter the time of the task to remove (HH:MM): ")
        if time in tasks:
            del tasks[time]
            print(f"Task at {time} removed.")
        else:
            print(f"No task found at {time}.")
    elif choice == "show":
        if tasks:
            print("Current tasks:")
            for time, task in tasks.items():
                print(f"{time}: {task}")
        else:
            print("No tasks scheduled.")
    elif choice == "exit".lower().upper():
        print("Exiting the task planner. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 'add', 'remove', 'show', or 'exit'.")
    print() 
    print("Current tasks:")
    for time, task in tasks.items():
        print(f"{time}: {task}")