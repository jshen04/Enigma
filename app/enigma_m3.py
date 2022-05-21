from plug import BijectiveMap
from rotor import Rotor

class EnimgaM3:
    def __init__(self, reflector, rotor1, rotor2, rotor3, plugs):
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.reflector = reflector
        self.plugs = plugs

    def rotate(self):
        self.rotor1.rotate()
        if self.rotor1.rotor_wiring[0] == self.rotor1.trigger:
            self.rotor2.rotate()
            if self.rotor2.rotor_wiring[0] == self.rotor2.trigger:
                self.rotor3.rotate()

    def forward(self, s):
        ans = ""
        newS = self.plugs.link(s)
        for c in newS:
            if c.isalpha():
                self.rotate()
                x = self.rotor1.forward(c)
                n = self.rotor1.ring_position.index(x)
                x = self.rotor2.forward(self.rotor2.ring_position[n])
                n = self.rotor2.ring_position.index(x)
                x = self.rotor3.forward(self.rotor3.ring_position[n])
                x = self.reflector.forward(x)
                x = self.rotor3.backward(x)
                n = self.rotor3.ring_position.index(x)
                x = self.rotor2.backward(self.rotor2.ring_position[n])
                n = self.rotor2.ring_position.index(x)
                x = self.rotor1.backward(self.rotor1.ring_position[n])
                ans = ans + x
            else:
                ans = ans + c
        return self.plugs.link(ans)
    

b2 = BijectiveMap('AB','ZC')
r1 = Rotor('A', 'V', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ')
r2 = Rotor('A', 'E', 'AJDKSIRUXBLHWTMCQGZNPYFVOE')
r3 = Rotor('A', 'Q', 'BDFHJLCPRTXVZNYEIWGAKMUSQO')
reflector = Rotor('A', 'A', 'FVPJIAOYEDRZXWGCTKUQSBNMHL')

e1 = EnimgaM3(reflector, r3, r2, r1,b2)
print(e1.forward('ABC'))
