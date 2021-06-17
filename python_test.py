x = [100,110,120,130,140,150]
z=[x*5 for x in x]
print(z)

def divisible_by_three(n):
    x=range(1,n)
    for x in x:
        if x%3==0:
            print(x)
divisible_by_three(30)


x = [[1,2],[3,4],[5,6]]


def smallest(*args):
    smallNo=min(args)
    print(smallNo)
smallest(20,10,38,5,15,2)

def duplicate():
    x = ['a','b','a','e','d','b','c','e','f','g','h']
    y=set(x)
    x=list(y)
    print(x)
duplicate()

  
def greet():
    students = [{"age": 19, "name": "Eunice"},
     {"age": 21, "name": "Agnes"},
     {"age": 18, "name": "Teresa"}, 
     {"age": 22, "name": "Asha"}]
    for student in students:
        print("Hello {} you were born in year {}".format(student["name"],2021-student["age"]))
greet()
    
class Rectangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length
    def area(self):
        A=self.length*self.width
        print(A)
    def perimeter(self):
        P=2*(self.length+self.width)
        print(P)
rectangle1=Rectangle(5,9)
rectangle1.area()
rectangle1.perimeter()


    
