# The Enigma Machine by Team J'lengima (Jeremy Shen and Justin Zou)

## What we did
- Essentially we made an encoder and decoder with the enigma machine.
- Our machine will allow you to encode and decode where you are able to set rotors, ring settings, plugboard, and reflectors

## What is the Enigma Machine and some history
- The first enigma machine was made in the 20th century by German engineer Arthur Scherbius in 1918, who sought to sell it for commercial, rather than military, purposes
- Since then, many versions of the enigma machine have been made through the years, the most infamous of which is the German M3 which was used during WW2

![Arthur Scherbius](https://github.com/jshen04/Enigma/blob/main/imgs/arthur.jpg)

# So how did we make this encoder
- The enigma machine is made up of many moving and complicated parts that would have made it nearly impossible to crack it so we made an encoder and decoder instead. The hardest part by far of this project are the Rotors. The dictate the input and output of our strings and rotate each time giving us different outputs each time despite inputting the same string.
  - Something to realize is that each rotor has a default starting string which you can essentilaly hardcode in your code along with a similar set of reflectors.

![Enigma](https://github.com/jshen04/Enigma/blob/main/imgs/enigma.jpg)
## How do the Rotors work
Lets say you have the following as your rotor defaults:

| Rotor #      | ABCDEFGHIJKLMNOPQRSTUVWXYZ  |
| ----------- | ----------- |
| IC      | DMTWSILRUYQNKFEJCAZBPGXOHV       |
| IIC   | HQZGPJTMOBLNCIFDYAWVEUSRKX        |
| IIIC  |  UQNTLSZFMREHDPXKIBVYGJCWOA | 


And you select the letter A, you see that A goes on to D looking at the first rotor, then you plug D into the second rotor which returns G, and then you plug G into the third rotor to get Z. So that is how the tracing of the rotors work. The rotors themselves have a default starting string which then shifts over by one after each tracing. So as stated before after we plugged in A to get Z, the first rotor IC would then go from ```DMTWSILRUYQNKFEJCAZBPGXOHV``` over to ```MTWSILRUYQNKFEJCAZBPGXOHVD```. After this happens 26 times to the first rotor, the second rotor would then shift over by 1 as well, and after the second rotor shifts over 26 times the third rotor shifts over by 1 as well. This gives us a total of 26^3 total characters before we repeat a word.

![Rotors](https://github.com/jshen04/Enigma/blob/main/imgs/wheels.png)
### Reflectors 
Reflectors are essentially rotors that have an extra step of reflecting the output through the rotors. To put this in better terms, after we get from A to Z after passing through the three rotors at the beginning, You would then input Z into the reflector. 
| Rotor #      | ABCDEFGHIJKLMNOPQRSTUVWXYZ  |
| ----------- | ----------- |
| Reflector B |	YRUHQSLDPXNGOKMIEBFZCWVJAT 	|

Get an output of T and then input T back through the rotors to get back the final output of Q.

## Plugboard
The plugboard is a simple 1 to 1 mapping of letters. For example, if you plug A and Z together, it means that every instance of A was replaced with Z. For example if A was linked to Z and we plugged in ABC into our enigma machine it would return NHR. This would be the exact same output if we plugged in ZBC without the plugboard link.

![Plugboard](https://github.com/jshen04/Enigma/blob/main/imgs/plugboard.jpg)

## Ring Setting
Ring setting changes the internal wiring of the enigma rotors. The default ring setting is 0 which means nothing is changed and goes up to 25. Each number represents a letter of the alphabet with A being represented by 0 and Z being represented 25. Lets say we had a ring setting of 1, which is the first ring setting that changes something and we are using the rotor string ```DMTWSILRUYQNKFEJCAZBPGXOHV```. With a ring setting of B or 1, we have to shift up all the letters in the string by the ring setting. So if the ring setting is 1, every letter in the rotor string goes up by one. It means B would go to C, C would go to D, etc. So a string ```ekmflgdqvzntowyhxuspaibrcj``` would go to ```flngmherwaoupxziyvtqbjcsdk```. Each time we shift over the letters of the alphabet, we would then have to rotate our rotor over that many times. In this case we would have to rotate over once since our ring stetting is B and we shifted the letters once. So in our example this would mean that B becomes C and then is shifted over one spot. Essentially each ring setting is shifting the wiring by one and then rotating it. If the ring setting is 12 then we do it 12 times.

## Positioning
The default configuration for the enigma machine rotors is A,A,A. Each subsequent increase in the letters would mean a corresponding rotating on the wiring part. This means that A,A,B is the same thing as rotating the rotor once. These letters give a way of keeping track of the number of times the rotor has rotated and also help with increased randomization and were the letters that were given to the Germans when encrypting their code.

## Cracking the Enigma Machine
Cracking the enigma machine is a monumental task and very complex as you can tell by all the parts of the Enigma Machine. However, one viable way is through Artificial Intelligence and you can find out more information about it [here](https://github.com/greydanus/crypto-rnn). One of our group members, Jeremy Shen is a top 39 robotics engineer and top 3 in robot coordination in the world. If you have any questions please ask them.

# THANK YOU!




