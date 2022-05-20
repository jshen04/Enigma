from array import array
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
        for i in range(len(self.input1)):
            dict[self.input1[i].lower()] = self.input2[i].lower()
        for i in range(len(self.input1)):   
            dict[self.input2[i].lower()] = self.input1[i].lower()
        for k in s:
            newvalue = dict[k.lower()]
            print(newvalue)
            newOutput += newvalue
        return newOutput




        
