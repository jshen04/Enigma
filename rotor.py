import string

class Rotor:
    def __init__(self, ring_setting: str, notch: str, rotor_config: str):
        self.rotor_wiring = ''.join(rotor_config.split())
        self.ring_position = string.ascii_uppercase
        self.trigger = notch

        for _ in range(string.ascii_uppercase.index(ring_setting.upper())):
            self.shift()

    def rotate(self):
        self.rotor_wiring = self.rotor_wiring[1:] + self.rotor_wiring[0]
        self.ring_position = self.ring_position[1:] + self.ring_position[0]

    def shift(self):
        for i, c in enumerate(self.rotor_wiring):
            self.rotor_wiring =  self.rotor_wiring[0:i] + chr(((ord(c) + 1) - 65 ) % 26 + 65) + self.rotor_wiring[i+1:]

    def forward(self, c):
        return self.rotor_wiring[string.ascii_uppercase.index(c.upper())]

    def backward(self, c):
        return string.ascii_uppercase[self.rotor_wiring.index(c.upper())]