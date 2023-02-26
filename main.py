# Netology. First Program
import random
# Дата в Python не является типом данных, но мы можем импортировать модуль с именем datetime для работы с датами
import datetime

# def my_date_function(i):
#     if i == 3:
#         i = "if"
#     else:
#         i = "else"
#     return i
# x = my_date_function(3)
# print("Return from my_date_function: ", x)

# def multiply(a,b):
#     result = a + b
#     return result
#
# c = multiply(1, 1)
# print(c)
# c = multiply(5, 5)
# print(c)

# def print_2():
#     print("Print something")
# print_2()

from datetime import timedelta
date_now_temp = datetime.datetime.now()
# Урезаем до даты, микросекудны нам без надобности
# print(x.date())
date_now = date_now_temp.strftime("%d%m%Y")
date_tomorrow_temp = date_now_temp + timedelta(days=1)
date_tomorrow = date_tomorrow_temp.strftime("%d%m%Y")

print("Today: ", date_now, "Tomorrow will be: ", date_tomorrow)

# Вынес код по времени в отдельную функцию
def my_date_input_func():
    import datetime as dt
    date_str = input("Input the date to show the task list (ddmmyyyy): \n")
    data_temp = dt.datetime.strptime(date_str, '%d%m%Y').date()
    data_to_list = data_temp.strftime("%d%m%Y")
    print("You entered the date: ", data_to_list)
    print("Функция времени отрабатывает, возвращаем: ", data_to_list)
    return data_to_list

# Тройные кавычки позволяют создать одну строчку разделенную на несколько
HELP = """
help        - print a reference
add         - add a task into the list (enter the date "01012001" for random function)
show/sh     - print all added tasks
random/r    - add random task for today date;
exit/quit/q - quit the program \n"""
print(HELP)

# Task 1. Creation of the empty lists
today = list()
tomorrow = []
other = []
random_list = ["Учится", "Любить", "Забоиться", "Оберегать", "Гладить"]
random_scheduled = list()
RANDOM_TASK = "Временная задача, удалить потом. См. выше"
# Improvements, dictionary
tasks = {

}

# Number of tasks the user can input = X = 3 pieces (pcs.)
# x = 0
# while x < 3:
#     print("Number of tasks added: ", x)
#     x = x + 1

goodbye: str = "\tСпасибо за использование! До свидания!"
run = True

while run:
      command = input("Input command: ")
      if command == "help":
          print(HELP)

      elif command == "show" or command == "sh":
          print('\nDictionary "Tasks": ', tasks, "\nToday: ", today, "\nTomorrow: ", tomorrow, "\nOther: ", other, "\nRandom: ", random_scheduled)

          # the cicle "for". if the remainder of division = 0 so the number is "even number" (четное)
          # for element in [4, 5, 6]:
          #     if element % 2 == 0:  # ramainder of divistion (остаток от деления)
          #         print(element)

          # import datetime as dt
          # date_str = input("Input the date to show the task list (ddmmyyyy): \n")
          # data_temp = dt.datetime.strptime(date_str, '%d%m%Y').date()
          # data_to_list = data_temp.strftime("%d%m%Y")
          # print("You entered the date: ", data_to_list)

          data_to_list = my_date_input_func()
          print("Вернули из фунцкии", data_to_list)

          # Add "-" before the tasks
          if data_to_list in tasks:
              for task in tasks[data_to_list]:
                print('- ', task)
          else:
              print('No such date')
      elif command == "add":
              # import datetime as dt
              # date_str = input("Input the date (ddmmyyyy): \n")
              # data_temp = dt.datetime.strptime(date_str, '%d%m%Y').date()
              # data_to_list = data_temp.strftime("%d%m%Y")
              # print("You entered the date: ", data_to_list)

              # Remove data processing to function
              data_to_list = my_date_input_func()
              print("Вернули из фунцкии", data_to_list)

              task = input("Input the name of the task (fro random - no need): ")

              if data_to_list == date_now:
                  today.append(task)

                  # Check if the key "data_to_list" already exists in the dictonary "Tasks"
                  if data_to_list in tasks:
                      # The data is in the dictonary, we add the task
                      tasks[data_to_list].append(task)
                  else:
                      # The data is not in the dictionary, so we create data key and the task for it
                      tasks[data_to_list] = [task]
                  print("The task added to TASKS Dictionary: ", tasks)
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

      elif (command == "random") or (command == "r"):

          data_to_list = my_date_input_func()
          print("Вернули из фунцкии", data_to_list)

          # import datetime as dt
          # date_str = input("Input the date to show the task list (ddmmyyyy): \n")
          # data_temp = dt.datetime.strptime(date_str, '%d%m%Y').date()
          # data_to_list = data_temp.strftime("%d%m%Y")
          # print("You entered the date: ", data_to_list)

          if data_to_list in tasks:
              tasks[data_to_list].append(RANDOM_TASK)
              print(tasks)
          else:
              tasks[data_to_list] = [RANDOM_TASK]
              print("The task added to TASKS Dictionary: ", tasks)

      elif (command == "exit") or (command == "quit") or (command == "q"):
          print("Exit ok")
          break

      else:
          print("Unknown command")
          # abort the loop if an unknow command is entered
          print(HELP)
          #run = False

print(goodbye)