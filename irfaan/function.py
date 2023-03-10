import render

def function():
    print("hello")
    print("function")
    
def add_sub(x,y):
    c = (x+y*x)
    d=x-y
    return c,d

function()
result1,result2 = add_sub(12,8)
print(result1,result2)



def update(sec):
    print(id(sec))
    sec[0]=22
    print("x",sec)

sec=[11,22,33]
print(id(sec))
update(sec)
print("sec",sec)

def person(name,age,native,college):
    print(name)
    print(age)
    print(college)
    print(native)
  

person(age=21,name='irfaan',native='chennai',college='sathak college' )

def sums(a,*b):
  
  print(a)
  print(b)

sums(26,22,25,27)
def sum(a,b):
    c=a+b
    print(c)
sum(23,27)

def app(a, *b):
    c=a
     
    for i in b:
        c=c+i
    print(c)

app(23,21,11,5)


def mini(name, **data):
    print(name)
   
    for i,j in data.items():
        print(i,j)

mini('navin',age=28,city='chennai',num=1234556)    

a=21
print(id(a))
def something():
    a=76
    
    x=globals()['a']
    print(id(x))
    print("inside",a)
    
something()

print("outside",a)

def count(lst):
    
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

 
lst=[21,34,88,52,18,49,77,17,54,23]
even,odd=count(lst)

print("even:{} and odd:{}".format(even,odd))


def fib(n):
    a=0
    b=5
   
    print(a)
    print(b)
    for c in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
fib(10)



print("sala",__name__)

class computer():
    def __init__(self):
        print("in init")


    def config(self):
        print("i6,34gb,2TB")

com1 =computer()
com2 =computer()



com1.config()
com2.config()

class definition():
    def __init__(self):
        self.name="irfaan"
        self.age=21
        

    def update(self):
        self.age=26

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False



c1=definition()
c2=definition()

if c1.compare(c2):
    print("They are same")

 


print(c1.name)
print(c2.age)

def function(request):
    receivedinput =request.POST['calci']
    if receivedinput =="":
        return render (request,"index.html")