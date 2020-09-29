class A:
    def __init__(self):
        self.a = 25
        self.name = "Giles Simon"
        print("My age is {} and My name is {}".format(self.a, self.name))
        print("I will be called when an object for this class is created")


object = A()
