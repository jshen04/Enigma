import string

class BijectiveMap:

    def __init__(self, input1:str, input2:str):
        self.input1 = input1
        self.input2 = input2

    def link(self):
        dict = {}
        dict[self.input1] = self.input2
        
