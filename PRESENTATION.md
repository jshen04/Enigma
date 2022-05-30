# The Enigma Machine by Team J'lengima (Jeremy Shen and Justin Zou)

## What we did
- Essentially we made an encoder and decoder with the enigma machine.
- Our machine will allow you to encode and decode where you are able to set rotors, ring settings, plugboard, and reflectors

## What is the Enigma Machine and some history
- The first enigma machine was made in the 20th century by German engineer Arthur Scherbius in 1918, who sought to sell it for commercial, rather than military, purposes
- Since then, many versions of the enigma machine have been made through the years, the most infamous of which is the German M3 which was used during WW2

# So how did we make this encoder
- The enigma machine is made up of many moving and complicated parts that would have made it nearly impossible to crack it so we made an encoder and decoder instead. The hardest part by far of this project are the Rotors. The dictate the input and output of our strings and rotate each time giving us different outputs each time despite inputting the same string.
  - Something to realize is that each rotor has a default starting string which you can essentilaly hardcode in your code along with a similar set of reflectors.

## How do the Rotors work
Lets say you have the following as your rotor defaults:

| Rotor #      | ABCDEFGHIJKLMNOPQRSTUVWXYZ  |
| ----------- | ----------- |
| IC      | DMTWSILRUYQNKFEJCAZBPGXOHV       |
| IIC   | HQZGPJTMOBLNCIFDYAWVEUSRKX        |
| IIIC  |  UQNTLSZFMREHDPXKIBVYGJCWOA | 


And you select the letter A, you see that A goes on to D looking at the first rotor, then you plug D into the second rotor which returns G, and then you plug G into the third rotor to get Z. So that is how the tracing of the rotors work. The rotors themselves have a default starting string which then shifts over by one after each tracing. So as stated before after we plugged in A to get Z, the first rotor IC would then go from ```DMTWSILRUYQNKFEJCAZBPGXOHV``` over to ```MTWSILRUYQNKFEJCAZBPGXOHVD```. After this happens 26 times to the first rotor, the second rotor would then shift over by 1 as well, and after the second rotor shifts over 26 times the third rotor shifts over by 1 as well.

### Reflectors 
Reflectors are essentially rotors that have an extra step of reflecting the output through the rotors. To put this in better terms, after we get from A to Z after passing through the three rotors at the beginning, You would then input Z into the reflector. 
| Rotor #      | ABCDEFGHIJKLMNOPQRSTUVWXYZ  |
| ----------- | ----------- |
| Reflector B |	YRUHQSLDPXNGOKMIEBFZCWVJAT 	|

Get an output of T and then input T back through the rotors to get back the final output of Q.

## Plugboard
The plugboard is a simple 1 to 1 mapping of letters. For example, if you plug A and Z together, it means that every instance of A was replaced with Z. For example if A was linked to Z and we plugged in ABC into our enigma machine it would return NHR. This would be the exact same output if we plugged in ZBC without the plugboard link.

## Ring Setting
Ring setting is something that was not really covered in the videos we watched but essentially they are another layer of complexity. The default ring setting is 1 which means nothing is changed and goes up to 26. If the ring setting is 2, every letter in the rotor string goes up by one. So if B would go to C, C would go to D, etc. So a string ```ekmflgdqvzntowyhxuspaibrcj``` would go to ```flngmherwaoupxziyvtqbjcsdk```.






