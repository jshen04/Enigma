# The Enigma Machine by Team J'lengima (Justin Zou and Jeremy Shen)

## What we did
- Essentially we made an encoder and decoder with the enigma machine.
- Our machine will allow you to encode and decode where you are able to set rotors, ring settings, plugboard, and reflectors

# What is the Enigma Machine
- The first enigma machine was made in the 20th century by German engineer Arthur Scherbius in 1918, who sought to sell it for commercial, rather than military, purposes
- Since then, many versions of the enigma machine have been made through the years, the most infamous of which is the German M3 which was used during WW2

# So how did we make this encoder
- Something to realize is that each rotor has a default staring string which you can essentilaly hardcode in your code along with a similar set of reflectors.

# How do the Rotors work
Lets say you have 

| Rotor #      | ABCDEFGHIJKLMNOPQRSTUVWXYZ  |
| ----------- | ----------- |
| IC      | DMTWSILRUYQNKFEJCAZBPGXOHV       |
| IIC   | HQZGPJTMOBLNCIFDYAWVEUSRKX        |
| IIIC  |  UQNTLSZFMREHDPXKIBVYGJCWOA | 
and you select the letter A, you see that A goes on to D looking at the first rotor, then you plug D into the second rotor which returns G, and then you plug G into the third rotor to get Z. 




