class Student:
    school="AkiraChix"
    def __init__(self,firstName,lastName, age):
        self.firstName=firstName
        self.lastName=lastName
        self.age=age
    def speak(self):

      return f"Hello class, my name is {self.firstName}"

    def year_of_birth(self):

      return f"Hello class i am born in {2021-self.age}"
    def greeting(self):
      return f"Hello {self.firstName}, welcome to {self.school}"
    def initials(self):
      return f"Hello {self.firstName} {self.lastName} your initials are {self.firstName[0]} {self.lastName[0]}"

      
                 