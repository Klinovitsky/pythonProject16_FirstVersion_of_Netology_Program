# Netology. First Program
import random

# Дата в Python не является типом данных, но мы можем импортировать модуль с именем datetime для работы с датами
import datetime
from datetime import timedelta
date_now_temp = datetime.datetime.now()
# Урезаем до даты, микросекудны нам без надобности
# print(x.date())
date_now = date_now_temp.strftime("%d%m%Y")
date_tomorrow_temp = date_now_temp + timedelta(days=1)
date_tomorrow = date_tomorrow_temp.strftime("%d%m%Y")

print("Today: ", date_now, "Tomorrow will be: ", date_tomorrow)

# Тройные кавычки позволяют создать одну строчку разделенную на несколько
HELP = """
help        - print a reference
add         - add a task into the list (enter the date "01012001" for random function)
show/sh     - print all added tasks
exit/quit/q - quit the program \n"""
print(HELP)

# Task 1. Creation of the empty lists
today = list()
tomorrow = []
other = []
random_list = ["Учится", "Любить", "Забоиться", "Оберегать", "Гладить"]
random_scheduled = list()

# Number of tasks the user can input = X = 3 pieces (pcs.)
# x = 0
# while x < 3:
#     print("Number of tasks added: ", x)
#     x = x + 1

goodbye: str = "\tСпасибо за использование! До свидания!"
run = True
run_data = True

while run:
      command = input("Input command: ")
      if command == "help":
          print(HELP)

      elif command == "show" or command == "sh":
          print("\nTODAY: ", today, "\nTomorrow: ", tomorrow, "\nOther: \n", other, "\nRandom: \n", random_scheduled)

      elif command == "add":
          # while run_data:
              import datetime as dt
              date_str = input("Input the date (ddmmyyyy): \n")
              data_temp = dt.datetime.strptime(date_str, '%d%m%Y').date()
              data_to_list = data_temp.strftime("%d%m%Y")
              print("You entered the date: ", data_to_list)
              task = input("Input the name of the task (fro random - no need): ")

              if data_to_list == date_now:
                  today.append(task)
                  print("The task added to TODAY list: ", today)
              elif data_to_list == date_tomorrow:
                  tomorrow.append(task)
                  print("The task added to TOMORROW list: ", tomorrow)
              # test random function
              elif data_to_list == "01012001":
                  task = random.choice(random_list)
                  random_scheduled.append(task)
                  print(f'Random task is: "{task}"')
              else:
                  other.append(task)
                  print("The task added to OTHER list: ", other)
              print(f'The task: "{task}" added')
              print(HELP)

              # print("\nToday: ", today, "\nTomorrow: ", tomorrow, "\nOther: ", other)
              # if data_to_list == date_now:
              #     today.append(data_to_list)
              #     print("Index: ", today[0])
              #     task = input("Input the name of the task: ")
              #     today.append(task)
              #     print("The task added to TODAY list.", today)
              # elif data_to_list == date_tomorrow:
              #     tomorrow.append(data_to_list)
              #     task = input("Input the name of the task: ")
              #     tomorrow.append(task)
              #     print("The task added to TOMORROW list: ", tomorrow)
              # elif data_to_list != date_now or date_tomorrow:
              #     other.append(data_to_list)
              #     task = input("Input the name of the task: ")
              #     other.append(task)
              #     print("The task added to OTHER list.", other)
              # else:
              #     print("\nToday: ", today, "\nTomorrow: ", tomorrow, "\nOther: ", other)

      elif (command == "exit") or (command == "quit") or (command == "q"):
          print("Exit ok")
          break

      else:
          print("Unknown command")
          # abort the loop if an unknow command is entered
          print(HELP)
          #run = False

print(goodbye)