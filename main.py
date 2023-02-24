# Netology. First Program

# Дата в Python не является типом данных, но мы можем импортировать модуль с именем datetime для работы с датами
import datetime
date_now_temp = datetime.datetime.now()
# Урезаем до даты, микросекудны нам без надобности
# print(x.date())
date_now = date_now_temp.strftime("%d-%m-%Y")
print("Today is: ", date_now)

# Тройные кавычки позволяют создать одну строчку разделенную на несколько
HELP = """
help - print a reference
add  - add a task into the list
show - print all added tasks
exit - Quit the program"""
print(HELP)

# Creation of the empty list
tasks = []
# Task 1. Creation lists
today = []
tomorrow = []
other = []

# Number of tasks the user can input = X = 3 pieces (pcs.)
# x = 0
# while x < 3:
#     print("Number of tasks added: ", x)
#     x = x + 1

goodbye: str = "\tСпасибо за использование! До свидания!"
run = True
# run_data = True

while run:
      command = input("Input command: ")
      if command == "help":
          print(HELP)
      elif command == "show":
          print("Today: ", today, "Tomorrow: ", tomorrow, "Other: ", other)

      elif command == "add":
          # while run_data:
              import datetime as dt
              date_str = input("Введите дату (dd-mm-yyyy)\n")
              data_temp = dt.datetime.strptime(date_str, '%d-%m-%Y').date()
              data_to_list = data_temp.strftime("%d-%m-%Y")
              print("You entered the date: ", data_to_list)

              if data_to_list == date_now:
                  today.append(data_to_list)
                  task = input("Input the name of the task: ")
                  today.append(task)
                  print("The task added to TODAY list.")
                  print(today)
              elif data_to_list > date_now:
                  other.append(data_to_list)
                  task = input("Input the name of the task: ")
                  other.append(task)
                  print("The task added to OTHER list.")
                  print(other)

              print("Today: ", today, "Tomorrow: ", tomorrow, "Other: ",  other)

      elif command == "exit":
          print("Exit ok")
          break
      else:
          print("Unknown command")
          # abort the loop if an unknow command is entered
          break
          #run = False

print(goodbye)