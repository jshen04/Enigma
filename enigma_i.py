from rotor import Rotor

class EnimgaI:
    def __init__(self, reflector, rotor1, rotor2, rotor3):
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.reflector = reflector

    def rotate(self):
        self.rotor3.rotate()
        if self.rotor3.rotor_wiring[0] == self.rotor3.trigger:
            self.rotor2.rotate()
            if self.rotor2.rotor_wiring[0] == self.rotor2.trigger:
                self.rotor1.rotate()

    def forward(self, s):
        ans = ""
        for c in s:
            if c.isalpha():
                print(c)
                x = self.rotor3.forward(c)
                print(x)
                x = self.rotor2.forward(x)
                print(x)
                x = self.rotor1.forward(x)
                print(x)
                x = self.reflector.forward(x)
                print(x)
                x = self.rotor1.backward(x)
                print(x)
                x = self.rotor2.backward(x)
                print(x)
                ans = ans + self.rotor3.backward(x)
                print(x)
                self.rotate()
            else:
                ans = ans + c
        return ans

r1 = Rotor('A', 'AJDKSIRUXBLHWTMCQGZNPYFVOE')
r2 = Rotor('B', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ')
r3 = Rotor('L', 'BDFHJLCPRTXVZNYEIWGAKMUSQO')
reflector = Rotor('A', 'EJMZALYXVBWFCRQUONTSPIKHGD')

e1 = EnimgaI(reflector, r1, r2, r3)
print(e1.forward('P'))

