class Class:
    variable_1 = 0
    variable_2 = 'str'

    def __init__(self):
        print("I've been constructed.")

    def method(self):
        self.variable_1 = self.variable_1 + 1
        return self.variable_1
        print("So far x =", self.variable_1) # object is 'self-variable_1'

    def __del__(self):
        print("I've been deconstructed. So far, x =", method())

an = Class()
an.method()
