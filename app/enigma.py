# Create your own enigma machine
# Maybe this can be an abstract enigma class?
from plug import Plug
from rotor import Rotor

class Enigma:
    def __init__(self, reflector: Rotor, rotors: list, plugs: Plug):
        self.reflector = reflector
        self.rotors = rotors
        self.plug = plugs

        self.numRotors = len(rotors)

    def rotate(self):
        for rotor in self.rotors:
            rotor.rotate()
            if rotor.rotor_wiring[0] != rotor.trigger:
                break

    def forward(self, s):
        ans = ""
        s = self.plug.link(s)
        for c in s:
            if c.isalpha():
                self.rotate()
                c = self.rotors[0].forward(c)
                n = self.rotors[0].ring_position.index(c)
                for rotor in self.rotors[1:]:
                    c = rotor.forward(rotor.ring_position[n])
                    n = rotor.ring_position.index(c)
                c = self.reflector.forward(c)
                c = self.rotors[-1].backward(c)
                n = self.rotors[-1].ring_position.index(c)
                for rotor in reversed(self.rotors[:-1]):
                    c = rotor.backward(rotor.ring_position[n])
                    n = rotor.ring_position.index(c)
                ans = ans + c
            else:
                ans = ans + c
        return self.plug.link(ans)