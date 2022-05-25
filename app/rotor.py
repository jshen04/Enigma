from collections import Counter
import string


class Rotor:
    def __init__(self, ring_setting: str, position: str, rotor_config: str, notch: str):
        self.rotor_wiring = ''.join(rotor_config.upper().split())
        self.ring_position = string.ascii_uppercase
        self.trigger = notch.upper()

        if len(ring_setting) != 1 or not ring_setting.isalpha():
            raise ValueError("ring setting must be one letter")

        if len(position) != 1 or not position.isalpha():
            raise ValueError("start position must be one letter")

        if len(notch) != 1 or not notch.isalpha():
            raise ValueError("notch must be one letter")

        if len(self.rotor_wiring) != 26 or len(Counter(self.rotor_wiring)) != 26:
            raise ValueError("rotor must use very letter in the alphabet exactly once")

        for _ in range(string.ascii_uppercase.index(ring_setting.upper())):
            self.shift()
            self.rotor_wiring = self.rotor_wiring[-1] + self.rotor_wiring[:-1]

        for _ in range(string.ascii_uppercase.index(position.upper())):
            self.rotate()

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