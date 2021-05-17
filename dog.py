class Dog:
    bark="wuhwuh"
    def __init__(self,eat,runs):
        self.eat=eat
        self.runs=runs
    def food(self):

      return f"Hello my dog likes {self.eat}"

    def speed(self):
      return f"His dog runs very {self.runs}"

