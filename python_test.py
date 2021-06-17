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


q=[10,20,7,5]
print(q[3])

x = ['a','b','a','e','d','b','c','e','f','g','h']
print(type(x))

  
def greet():
    students = [{"age": 19, "name": "Eunice"},
     {"age": 21, "name": "Agnes"},
     {"age": 18, "name": "Teresa"}, 
     {"age": 22, "name": "Asha"}]
    for student in students:
        print("Hello {} you were born in year {}".format(student["name"],2021-student["age"]))
greet()
    


    
