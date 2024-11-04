import random
class RandomArrayGenerator:
    def __init__(self,value = 100):
        self.value = value
        self.array = [random.randint(0,value) for i in range(value)]

