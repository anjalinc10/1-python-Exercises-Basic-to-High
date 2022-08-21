class Calculator():

    def __init__(self,num):
        self.num=num
    
    @staticmethod
    def greet():
        print("hello!")

    def square(self):
        print(f'square is {self.num**2}')
    
    def cube(self):
        print(f'cube is: {self.num**3}') 

    def squareroot(self):
        print(f'squareroot is{self.num**0.5}')

operate = Calculator(2)
operate.square()
operate.cube()
operate.squareroot()
operate.greet()