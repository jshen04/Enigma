import string

class Rotor:
    def __init__(self, start_key: str, rotor_config: str):
        self.rotor_wiring = ''.join(rotor_config.split())
        self.trigger = self.rotor_wiring[0]

        for _ in range(string.ascii_uppercase.index(start_key.upper())):
            self.rotate()

        # while self.rotor_wiring[0] != start_key:
        #     if self.rotor_wiring[0] == start_key:
        #         break
        #     self.rotate()

    def rotate(self):
        self.rotor_wiring = self.rotor_wiring[1:] + self.rotor_wiring[0]

    def forward(self, c):
        return self.rotor_wiring[string.ascii_uppercase.index(c.upper())]

    def backward(self, c):
        return string.ascii_uppercase[self.rotor_wiring.index(c.upper())]
