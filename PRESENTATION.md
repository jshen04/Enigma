# The Enigma Machine by Team J'lengima (Justin Zou and Jeremy Shen)

## What we did
- Essentially we made an encoder and decoder with the enigma machine.
- Our machine will allow you to encode and decode where you are able to set rotors, ring settings, plugboard, and reflectors

## What is the Enigma Machine and some history
- The first enigma machine was made in the 20th century by German engineer Arthur Scherbius in 1918, who sought to sell it for commercial, rather than military, purposes
- Since then, many versions of the enigma machine have been made through the years, the most infamous of which is the German M3 which was used during WW2

# So how did we make this encoder
- The enigma machine is made up of many moving and complicated parts that would have made it nearly impossible to crack it so we made an encoder and decoder instead. The hardest part by far of this project are the Rotors. The dictate the input and output of our strings and rotate each time giving us different outputs each time despite inputting the same string.
  - Something to realize is that each rotor has a default staring string which you can essentilaly hardcode in your code along with a similar set of reflectors.

# How do the Rotors work
Lets say you have the following as your rotor defaults:

| Rotor #      | ABCDEFGHIJKLMNOPQRSTUVWXYZ  |
| ----------- | ----------- |
| IC      | DMTWSILRUYQNKFEJCAZBPGXOHV       |
| IIC   | HQZGPJTMOBLNCIFDYAWVEUSRKX        |
| IIIC  |  UQNTLSZFMREHDPXKIBVYGJCWOA | 


And you select the letter A, you see that A goes on to D looking at the first rotor, then you plug D into the second rotor which returns G, and then you plug G into the third rotor to get Z. 

### Reflectors 
Reflectors are essentially rotors that have an extra step of reflecting the output through the rotors. To put this in better terms, after we get from A to Z after passing through the three rotors at the beginning, You would then input Z into the reflector. Get an output of lets say B and then input B back through the rotors to get back the final output.



