 import json

try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = []
except json.JSONDecodeError:
    expenses=[]
def save():
    with open("expenses.json", "w") as file:
        json.dump(expenses,file)
def show_total():
    tot=0
    for expense in expenses:
        tot+=expense['amount']
    print("Total expenses:", tot)
def view_expenses():
    for expense in expenses:
        print(expense['amount'],expense['category'],
        expense['desc'])
def add_expenses():
    while True:
        try:
            amount=int(input("amount"))
            if amount<=0:
                print("amound should be>0")
                continue
            break
        except ValueError:
            print("please enter a number")
    category=(input("category"))
    desc=(input("desc"))
    expense={ 
    "amount":amount,
    "category":category,
    "desc":desc}
    expenses.append(expense)
def delete_expenses():
    if not expenses:
        print("this list blank")
        return
    while True:
        for i in range(len(expenses)):
            print(i + 1, expenses[i])
        try:
            g=int(input("choose"))
            del expenses[g-1]
            break
        except ValueError:
            print("please choose from numbers that you have")
        except IndexError:
            print("you dont have that expence")
while True:
    print("1-add expenses",
           "2-View expenses",
           "3- Show total",
           "4-exit?",
          '5-delete expenses')
    choice=input('choose')
    if choice=="1":
        add_expenses()
        save()
    elif choice=='2':
        view_expenses()
    elif choice=="3":
        show_total()
    elif choice=="4":
        break
    elif choice=="5":
        delete_expenses()
        save()
print("Expense Tracker v1.1")
