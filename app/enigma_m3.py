from enigma import Enigma
from plug import Plug
from rotor import Rotor

p = Plug('', '')
r1 = Rotor('A', 'A', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q')
r2 = Rotor('A', 'A', 'AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E')
r3 = Rotor('A', 'A', 'BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V')
reflector = Rotor('A', 'A', 'FVPJIAOYEDRZXWGCTKUQSBNMHL', 'A')
e1 = Enigma(reflector, [r3, r2, r1], p)
print(r1.rotor_wiring, r1.ring_position)
print(r2.rotor_wiring, r2.ring_position)
print(r3.rotor_wiring, r3.ring_position)

print(e1.forward("ABC"))



# class EnimgaM3:
#     def __init__(self, reflector, rotor1, rotor2, rotor3, plugs):
#         self.rotor1 = rotor1
#         self.rotor2 = rotor2
#         self.rotor3 = rotor3
#         self.reflector = reflector
#         self.plugs = plugs
#
#     def rotate(self):
#         self.rotor1.rotate()
#         if self.rotor1.rotor_wiring[0] == self.rotor1.trigger:
#             self.rotor2.rotate()
#             if self.rotor2.rotor_wiring[0] == self.rotor2.trigger:
#                 self.rotor3.rotate()
#
#     def forward(self, s):
#         ans = ""
#         s = self.plugs.link(s)
#         for c in s:
#             if c.isalpha():
#                 self.rotate()
#                 x = self.rotor1.forward(c)
#                 n = self.rotor1.ring_position.index(x)
#                 x = self.rotor2.forward(self.rotor2.ring_position[n])
#                 n = self.rotor2.ring_position.index(x)
#                 x = self.rotor3.forward(self.rotor3.ring_position[n])
#                 x = self.reflector.forward(x)
#                 x = self.rotor3.backward(x)
#                 n = self.rotor3.ring_position.index(x)
#                 x = self.rotor2.backward(self.rotor2.ring_position[n])
#                 n = self.rotor2.ring_position.index(x)
#                 x = self.rotor1.backward(self.rotor1.ring_position[n])
#                 ans = ans + x
#             else:
#                 ans = ans + c
#         return self.plugs.link(ans)
#
# p = Plug('AB', 'ZC')
# r1 = Rotor('A', 'V', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ')
# r2 = Rotor('A', 'E', 'AJDKSIRUXBLHWTMCQGZNPYFVOE')
# r3 = Rotor('A', 'Q', 'BDFHJLCPRTXVZNYEIWGAKMUSQO')
# reflector = Rotor('A', 'A', 'FVPJIAOYEDRZXWGCTKUQSBNMHL')
#
# e1 = EnimgaM3(reflector, r3, r2, r1, p)
# print(e1.forward('ABC'))
