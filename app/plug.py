from collections import Counter
import string

class Plug:
    def __init__(self, input1, input2):
        if len(input1) != len(input2):
            raise Exception("input1 and input2 must have same length")

        if len(Counter(input1 + input2)) != len(input1 + input2):
            raise Exception("input1 and input2 must have unique and different letters")

        self.input1 = input1
        self.input2 = input2
        self.mapping = {}
        for i in range(26):
            self.mapping[string.ascii_uppercase[i]] = string.ascii_uppercase[i]
        for i in range(len(self.input1)):
            self.mapping[self.input1[i].upper()] = self.input2[i].upper()
        for i in range(len(self.input1)):
            self.mapping[self.input2[i].upper()] = self.input1[i].upper()

    def link(self, s):
        ans = ""
        for c in s:
            c = self.mapping[c.upper()]
            ans += c
        return ans