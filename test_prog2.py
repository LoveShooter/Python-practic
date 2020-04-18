

def create_record(owner, task, priority):
    "Create record in to do list"
    record = {
        'owner_name': owner,
        'task_name': task,
        'priority': priority,
    }
    print(record)
    return record


def main_record():
        owner = input("Enter Owner Name: ")
        task = input("Enter Task name: ")
        priority = int(input("Choose Priority from 1 to 5: "))
        if priority < 1:
            print ("!Error! You've choosen a number less 1!!!")
        elif priority > 5:
            print ("!Error! You've choosen a number greater than 5!!!")
    create_record(owner, task, priority)

main_record()



def countFood():
    a = int(input())
    b = int(input())
    print("Всего", a+b, "шт.")
 
print("Сколько бананов и ананасов для обезьян?")
countFood()
 
print("Сколько жуков и червей для ежей?")
countFood()
 
print("Сколько рыб и моллюсков для выдр?")
countFood()