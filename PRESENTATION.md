# The Enigma Machine by Team J'lengima (Jeremy Shen and Justin Zou)

## What we did
- Essentially we made an encoder and decoder simulating the enigma machine.
- Our machine will allow you to encode and decode where you can set rotors, ring settings, plugboard, and reflectors

## What is the Enigma Machine and some history
- The first Enigma machine was made in the 20th century by German engineer Arthur Scherbius in 1918, who sought to sell it for commercial, rather than military, purposes
- Since then, many versions of the enigma machine have been made through the years, the most infamous of which is the German M3 which was used during WW2

![Arthur Scherbius](https://github.com/jshen04/Enigma/blob/main/imgs/arthur.jpg)

# So how did we make this encoder
- The enigma machine is made up of many moving and complicated parts that would have made it nearly impossible to crack it so we made an encoder and decoder instead. The hardest part by far of this project is the Rotors. They dictate the input and output of our strings and rotate each time which gives us different outputs each time despite inputting the same string.
  - Something to realize is that each rotor has a default starting string which you can essentially hardcode in your code to make it easier when coding this project.

![Enigma](https://github.com/jshen04/Enigma/blob/main/imgs/enigma.jpg)
## How do the Rotors work
Let's say you have the following as your rotor defaults:

| Rotor #      | ABCDEFGHIJKLMNOPQRSTUVWXYZ  |
| ----------- | ----------- |
| IC      | EKMFLGDQVZNTOWYHXUSPAIBRCJ       |
| IIC   | AJDKSIRUXBLHWTMCQGZNPYFVOE        |
| IIIC  |  BDFHJLCPRTXVZNYEIWGAKMUSQO | 


And you select the letter A, you see that A goes on to E looking at the first rotor, but that would be your first mistake. The rotors rotate right before your first input goes through so in this case, A would go to K. The letters go to a one to one correspondence with rotors with the first position of the input mapping to the first position of the rotor. Rotating is essentially moving the letter forward and putting the first letter to the back so you go from ```EKMFLGDQVZNTOWYHXUSPAIBRCJ``` over to ```KMFLGDQVZNTOWYHXUSPAIBRCJE```. After this happens 26 times to the first rotor, the second rotor would then shift over by 1 as well, and after the second rotor shifts over 26 times the third rotor shifts over by 1 as well. This gives us a total of 26^3 total characters before we repeat a word.

 After this first rotor swap, you then have to rotate the top part of the alphabet as well to compensate for the first rotor rotate. Then you plug K into the second rotor, and realize that K now has the position of 10 because of the rotation moving it forward which returns B. However, the rotors are no longer rotated, so if you plug in B it stays a B in the second position so for the third rotor you would get D. So that is how the tracing of the rotors works.

![Rotors](https://github.com/jshen04/Enigma/blob/main/imgs/rotor1.png)
### Reflectors 
Reflectors are essentially the end rotors that have the job of reflecting what it is given through the rotors again. To put this in better terms, after we get from A to D after passing through the three rotors at the beginning, D gets passed back into  
| Rotor #      | ABCDEFGHIJKLMNOPQRSTUVWXYZ  |
| ----------- | ----------- |
| Reflector C | FVPJIAOYEDRZXWGCTKUQSBNMHL  |

Get an output of J and then input J back through the rotors to get back the final output of T. This time you go from the rotor to the Alphabet, so J in rotor 3 maps to E in the alphabet.E in rotor 2 maps to Z in the alphabet but A in the rotated Alphabet and A in rotor 1 maps to U in the alphabet, but with the shift this maps to T which is our output.

## Plugboard
The plugboard is a simple 1-to-1 mapping of letters. For example, if you plug A and Z together, it means that every instance of A was replaced with Z. For example if A was linked to Z and we plugged in ABC into our Enigma machine it would return NHR. This would be the same output if we plugged in ZBC without the plugboard link.

![Plugboard](https://github.com/jshen04/Enigma/blob/main/imgs/plugboard1.png)
![Plugboard](https://github.com/jshen04/Enigma/blob/main/imgs/plugboard2.png)

## Ring Setting
Ring setting changes the internal wiring of the Enigma rotors. The default ring setting is 0 which means nothing is changed and goes up to 25. Each number represents a letter of the alphabet with A being represented by 0 and Z being represented by 25. Let's say we had a ring setting of 1, which is the first ring setting that changes something and we are using the rotor string ```DMTWSILRUYQNKFEJCAZBPGXOHV```. With a ring setting of B or 1, we have to shift up all the letters in the string by the ring setting. So if the ring setting is 1, every letter in the rotor string goes up by one. It means B would go to C, C would go to D, etc. So a string ```ekmflgdqvzntowyhxuspaibrcj``` would go to ```flngmherwaoupxziyvtqbjcsdk```. Each time we shift over the letters of the alphabet, we would then have to rotate our rotor over that many times. In this case, we would have to rotate over once since our ring setting is B and we shifted the letters once. So in our example, this would mean that B becomes C and then is shifted over one spot. Essentially each ring setting is shifting the wiring by one and then rotating it. If the ring setting is 12 then we do it 12 times.

![Rotors](https://github.com/jshen04/Enigma/blob/main/imgs/rotor2.png)
![Rotors](https://github.com/jshen04/Enigma/blob/main/imgs/rotor3.png)
## Positioning
The default configuration for the enigma machine rotors is A, A, A. Each subsequent increase in the letters would mean a corresponding rotating on the wiring part. This means that A, A, B is the same thing as rotating the rotor once. These letters give a way of keeping track of the number of times the rotor has rotated and also help with increased randomization and were the letters that were given to the Germans when encrypting their code.

## Cracking the Enigma Machine
Cracking the enigma machine is a monumental task and very complex as you can tell by all the parts of the Enigma Machine. However, one viable way is through Artificial Intelligence and you can find out more information about it [here](https://github.com/greydanus/crypto-rnn). Of course we would also have to talk about one of the most important innovations in cracking enigma, the turing machine. Invented by Alan Turing, he developed a complex code-breaking technique he named ‘Turingery’ that uses logic to decipher it. One of our group members, Jeremy Shen is a top 3 most outstanding robot coordination researcher in the world (this year). If you have any questions please ask him.

# THANK YOU!




