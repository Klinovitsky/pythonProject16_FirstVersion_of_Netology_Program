# Netology. First Program
# Тройные кавычки позволяют создать одну строчку разделенную на несколько
HELP = """
help - print a reference
add  - add a task into the list
show - print all added tasks."""

print(HELP)

# Creation of the empty list
tasks = []

x = 0
while x < 3:
    print("Number of tasks added: ", x)
    x = x + 1

    command = input("Input command: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print(tasks)
    elif command == "add":
        task = input("Input the name of the task: ")
        tasks.append(task)
        print("The task added.")
        print(tasks)

    else:
        print("\nUnknown command")
