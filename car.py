class Car:
    color="Black"
    def __init__(self,model,make):
        self.model=model
        self.make=make
    def move(self):

      return f"My car is {self.make}"

    def speed(self):

      return f"It has high speed because it is {self.model}"
