x = [100,110,120,130,140,150]
z=[x*5 for x in x]
print(z)

x=range(1,30)
for x in x:
    if x%3==0:
        print(x)
    elif x%3!=0:
        print("not divisible")
    else:
        print("not divisible")


x = [[1,2],[3,4],[5,6]]


q=[10,20,7,5]
print(q[3])

x = ['a','b','a','e','d','b','c','e','f','g','h']
print(type(x))

  
class Student:
    def __init__(self, name ,age):
        self.nam=name
        self.age=age

    def greet(self, name, age):
        year=2021-age
        return f"Hello {self.name} you are born in the year {self.age} "
  
    


    
