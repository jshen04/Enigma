import string

Rotor1 = 'DMTWSILRUYQNKFEJCAZBPGXOHV'
Rotor2 = "HQZGPJTMOBLNCIFDYAWVEUSRKX"
Rotor3 = "UQNTLSZFMREHDPXKIBVYGJCWOA"
alphabet = list(string.ascii_lowercase)

def returnRotor(input):
    for k in range(26):
        if input.lower() == alphabet[k]:
            firstInput = Rotor1[k]
    for k in range(26):
        if firstInput.lower() == alphabet[k]:
            secondInput = Rotor2[k]
    for k in range(26):
        if secondInput.lower() == alphabet[k]:
            LastInput = Rotor3[k]
    return LastInput


print(returnRotor('A'))
        

