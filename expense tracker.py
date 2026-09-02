"""rez=[]
for N in range(1,1000):
    n=bin(N)[2::]
    n1=n+str(n.count('1')%2)
    n2=n1+str(n1.count('1')%2)
    R=int(n2,2)
    if R>225:
        rez.append(N)

print(min(rez))"""


"""rez=[]
for N in range(10_000,100_000):
    n1=int(str(N)[2])+int(str(N)[4])+int(str(N)[0])
    n2=int(str(N)[1])+int(str(N)[3])
    R=str(min(n1,n2))+str(max(n1,n2))
    if int(R)==621:
        rez.append(N)
print(min(rez))"""




"""rez=[]
for N in range(100,1000):
    n1=int(str(N)[0])*int(str(N)[1])*int(str(N)[2])
    n2=int(str(N)[0])+int(str(N)[1])+int(str(N)[2])
    R=str(max(n1,n2))+str(min(n1,n2))
    if int(R)==24019:
        rez.append(N)
print(max(rez))"""
"""rez=[]
for N in range(10000,100000):
    n1=int(str(N)[0])+int(str(N)[2])+int(str(N)[4])
    n2=int(str(N)[1])+int(str(N)[3])
    R=str(min(n1,n2))+str(max(n1,n2))
    if int(R)==818:
        rez.append(N)
print(min(rez))"""


"""rez=[]
for N in range(1,10000):
    n=bin(N)[2::]
    n1=n+str(n.count("1")%2)
    n2=n1+str(n1.count("1")%2)
    R=int(n2,2)
    if R>43:
        rez.append(R)
print(min(rez))"""
    
'''rez=[]
for N in range(1,10000):
    n=bin(N)[2::]
    n1=n.replace("0","00")
    n2=n1.replace("1","11")
    R=int(n2,2)
    if R>63:
        rez.append(R)
print(min(rez))'''
"""rez=[]
for N in range(1,10000):
    n=bin(N)[2::]
    n1=n+str(n.count('1')%2)
    n2=n1+str(n1.count('1')%2)
    R=int(n2,2)
    if 20<=R<=50:
        rez.append(R)
print(len(rez))"""


"""rez=[]
for N in range(500,601):
    n=sorted(str(N))
    mx=n[2]+n[1]
    if "0" not in n:
        mn=n[0]+n[1]
    if n.count("0")==1:
        mn=n[1]+n[0]
    if n.count("0")==2:
        mn=n[2]+n[0]
    R=int(mx)-int(mn)
    if R==10:
        rez.append(N)
print(len(rez))




from itertools import product
cnt=0
for i in product("012345",repeat=6):
    a="".join(i)
    a=a.replace("1","x").replace("3","x").replace("5","x")
    if "0" not in a[0]:
        if a.count("0")==1 and "0x" not in a and "x0" not in a:
            cnt+=1
print(cnt)"""
"""rez=[]
for N in range(2,1000):
    if N%2==0:
        N=N//2
    else:
        N=N-1
    if N%5==0:
        N=N//5
    else:
        N=N-1
    if N%7==0:
        N=N//7
    else:
        N=N-1
    if N==6:
        rez.append(N)
print(len(rez))"""




"""for N in range(1000,10000):
    n1=int(str(N)[0])+int(str(N)[1])
    n2=int(str(N)[1])+int(str(N)[2])
    n3=int(str(N)[2])+int(str(N)[3])
    t=sorted([n1,n2,n3])
    R=str(t[1])+str(t[2])
    if int(R)==1315:
        rez.append(N)
print(max(rez))"""

"""rez=[]
for N in range(1,10000):
    n=bin(N)[2::]
    if str(n.count('1')%2)
    n2=n1+str(n1.count('1')%2)
    R=int(n2,2)
    if 20<=R<=50:
        rez.append(R)
print(len(rez))"""


"""rez=[]
for N in range(10000,100000):
    n=bin(N)[2::]
    n1=int(str(N)[0])+int(str(N)[2])+int(str(N)[4])
    n2=int(str(N)[1])+int(str(N)[3])
    R=(str(min(n1,n2)))+(str(max(n1,n2)))
    if int(R)==818:
        rez.append(N)
print(min(rez))"""


"""rez=[]
for N in range(1,1000):
    n=bin(N)[2::]
    if "0" in n:
        n=n.replace("0","00")
    if "1" in n:
        n=n.replace("1","11")
    R=int(n,2)
    if R>32:
        rez.append(R)
print(min(rez))"""

"""rez=[]
for N in range(800,900):
    n=sorted(str(N))#145 012 001
    g=n[2]+n[1]
    if "0" not in n[0]:
        mn=n[0]+n[1]
    if n.count("0")==1:
        mn=n[1]+n[0]
    if n.count("0")==2:
        mn=n[2]+n[1]
    R=int(g)-int(mn)
    if R==30:
        rez.append(N)
print(len(rez))"""


"""rez=[]
def chet(a):
    if a==0:
        return("0")
    st=""
    while a>0:
        st=str(a%4)+st
        a=a//4
    return(st)
for N in range(0,1000):
    n=chet(N)
    if N%2==0:
        n="12"+n+(chet(int(n[-1])*3))
    if N%2!=0:
        n='21'+n+'13'
    R=int(n,4)
    if R>50:
        rez.append(R)
print(min(rez))"""
"""rez=[]
for N in range(100,1000):
    n=str(N)
    n1=int(n[0])+int(n[1])
    n2=int(n[1])+int(n[2])
    g=sorted([n1,n2])
    R=str(g[0])+str(g[1])
    if int(R)==912:
        rez.append(N)
print(len(rez))"""


"""rez=[]
for N in range(300,900):#110,100,111
    n=sorted(str(N))
    if "0" not in n:
        mx=n[2]+n[1]
        mn=n[0]+n[1]
    if n.count("0")==1:
        mx=n[2]+n[1]
        mn=n[1]+n[0]
    if n.count("0")==2:
        mx=n[2]+n[1]
        mn=n[2]+n[0]
    G=int(mx)-int(mn)
    if int(G)==10:
        rez.append(N)
print(len(rez)) """


"""rez=[]
for N in range(1,1000):
    n=bin(N)[2::]
    if sum(map(int,n))%2==0:
        n='10'+n[2::]+"0"
    if n.count("1")%2!=0:
        n="11"+n[2::]+'1'
    R=(int(n,2))
    if R>40:
        rez.append(N)
print(min(rez))"""
    
        
"""rez=[]
for N in range(1,256):
    n=bin(N)[2::].zfill(8)
    n=n.replace("0","!").replace("1","0").replace("!","1")
    n=int(n,2)
    n=n-N
    if n==99:
        rez.append(N)
print(rez)"""



"""rez=[]
for N in range(1,256):
    n=bin(N)[2::].zfill(8)
    n=n[0]+n[1::].replace("0","!").replace("1","0").replace("!","1")
    n=int(n,2)
    n=n-N
    if n==109:
        rez.append(N)
print(rez)"""


"""rez=[]
for N in range(1,1000):
    n=bin(N)[2::]
    if n.count("1")> n.count("0"):
        n=n+"1" 
    else:
        n=n+"0"
    R=int(n,2)
    if R<43:
        rez.append(R)
print(max(rez))"""

"""rez=[]
for N in range(11,256):
    n=bin(N-10)[2::].zfill(8)
    n=n.replace("0","!").replace("1","0").replace("!","1")
    n=int(n,2)
    if n==166:
        rez.append(N)
print(rez)"""



"""rez=[]
for N in range(1,1000):
    n=bin(N)[2::]
    if n.count("1")>=4:
        n="1"+n[:-2:]+"11"
    else:
        n=n[3::]+"1"
    R=int(n,2)
    if R>60:
        rez.append(N)
print(min(rez))"""


"""rez=[]
for N in range(100,991):
    n=sorted(str(N))
    if "0" not in n:
        mx=n[2]+n[1]
        mn=n[0]+n[1]
    if n.count("0")==1:
        mx=n[2]+n[1]
        mn=n[1]+n[0]
    if n.count("0")==2:
        mx=n[2]+n[1]
        mn=n[2]+n[0]
    R=int(mx)-int(mn)
    if R==34:
        rez.append(N)
print(len(rez))"""


"""rez=[]
def tri(a):
    g=""
    while a>0:
        g=str(a%3)+g
        a=a//3
    return g
for N in range(10,1000):
    n=tri(N)
    if N%4==0:
        n=n+n[-3]+n[-2]+n[-1]
    else:
        n="1"+n+"20"
    R=int(n,3)
    if R>423:
        rez.append(R)
print(min(rez))"""




"""rez=[]
for N in range(1,1000):
    n=bin(N)[2::]
    if n.count("1")>n.count("0"):
        n=n+"1"
    else:
        n=n+"0"
    R=int(n,2)
    if R<43:
        rez.append(R)
print(max(rez))"""
"""rez=[]
for N in range(1,1000):
    n=bin(N)[2::]
    n1=n+n[-1]
    if n1.count("1")%2==0:
        n1=n1+"0"
    else:
        n1=n1+"1"
    if n1.count("1")%2==0:
        n1=n1+"0"
    else:
        n1=n1+"1"
    R=int(n1,2)
    if R>114:
        rez.append(N)
print(min(rez))"""

"""rez=[]
for N in range(1,1000):
    n=bin(N)[2::]
    n=n+(str(n.count("1")%2))
    n=n+(str(n.count("1")%2))
    R=int(n,2)
    if 340<=R<=650:
        rez.append(R)
print(len(set(rez)))"""

"""rez=[]
for N in range(1,1000):
    n=bin(N)[2::]
    n=n+(str(n.count("1")%2))
    n=n+(str(n.count("1")%2))
    R=int(n,2)
    if 120<=R<=160:
        rez.append(R)
print(len(rez))"""
"""rez=[]
def che(a):
    if a==0:
        return "0"
    g=""
    while a>0:
        g=str(a%4)+g
        a=a//4
    return g
for N in range(0,1000):
    n=che(N)
    if N%2==0:
        n='12'+n+che(int(n[-1])*3)
    else:
        n="13"+n+"21"
    R=int(n,4)
    if R>50:
        rez.append(R)
print(min(rez))"""


"""class cat:
    name= None
    age=None
    happy=None
    def set_data(self,name,age,happy):
        self.name=name
        self.age=age
        self.happy=happy
    def get_data(self):
        print(self.name,"age")
cat1=cat()
cat1.set_data("suka",10,True)
print(cat1.name"""


'''expenses=[]
    amount=int(input("amount"))
    category=(input("category"))
    desc=(input("desc"))
    answer=(input("add another expenses?"))
    expense={ 
    "amount":amount,
    "category":category,
    "description":desc}
    expenses.append(expense)
    print(expenses)'''
git--version
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
    print(tot)
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
        




















