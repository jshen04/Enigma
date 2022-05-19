import string

class BijectiveMap:

    def __init__(self, input1:str, input2:str):
        self.input1 = input1
        self.input2 = input2

    def link(self,s):
        alphabet = list(string.ascii_lowercase)
        newOutput = ""
        dict = {}
        for i in range(26):
           dict[alphabet[i]] = alphabet[i]
        dict[self.input1.lower()] = self.input2.lower()
        dict[self.input2.lower()] = self.input1.lower()
        for k in s:
            newvalue = dict[k.lower()]
            newOutput += newvalue
        return newOutput




        
