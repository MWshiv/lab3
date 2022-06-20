import json
task = []

def create(task):
    ta = input('Сформулируйте задачу: ')
    ca = input('Добавьте категорию к задаче: ')
    ti = input('Добавьте время к задаче: ')
    task.append("Задача: " + t + ", Категория: " + ca + ", Время: " + ti)
    task = str(task)
    with open('todo.json', 'w') as f:
       return json.dump(task, f)

print("Простой todo: \n 1. Добавить задачу. \n 2. Вывести список задач. \n 3. Выход.")

while True :
    t = input('Укажите число: ')
    if t == "1" :
        create(task)
        
    elif t == "2" :
        try:
            with open('todo.json') as f:
                numbers = json.load(f)
            print(numbers)
        except Exception as e:
            print(e)

    elif t == "3":
        print('Задачи сохранены в файл')
        break
    else:
        print("Такого числа нет в списке")
