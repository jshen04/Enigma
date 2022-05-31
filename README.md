# Enigma by Jeremy Shen and Justin Zou
Stuyvesant High School Spring 2022 Cybersecurity Final Project

## Project Description
This is our final project in Cybersecurity where we made an enigma machine encoder and decode. We built built all of the componenets of the machine up from scratch using just python. This includes the plugboard, rotors, reflectors and ring settings as well as inputs. To being look at the steps below.

## How to use it:
1. Git clone our repository
2. ```make default```
* This runs the default enigma machine setup (rotors 1, 2, 3 in that order; ring settings and positions: A; no plugs)
or 
2.```make custom ARGS="RotorNumber1 RingSetting1 Position1 RotorNumber2 RingSetting2 Position2 RotorNumber3 RingSetting3 Position3 Reflector [PlugsPairs]"```
* Where ```RotorNumber``` is an integer from 1-5 representing the physical rotor used in that slot, ```RingSetting``` is a letter corresponding to the ring setting of the respective rotor (depending on the codebook, you may need to convert integer to letter), ```Position``` is a letter representing the starting position of the respective rotor, ```Reflector``` is a letter corresponding to a physical rotor (A-C), and ```[PlugPairs]``` can be any amount of _pairs_ of letters representing the physical plugboard and letter swaps (remember that each letter may be used only once, and in real machines there were only 10 swaps).
or
2.```cd app```
5. ```python3 enigma_m3.py enigma_m3.py RotorNumber1 RingSetting1 Position1 RotorNumber2 RingSetting2 Position2 RotorNumber3 RingSetting3 Position3 Reflector [PlugsPairs]```
* Where the arguments are the same as those in the  prior make command ```make custom ARGS``` 

Example: ```python3 enigma_m3.py 5 F G 4 A D 1 W X B AB XS DF TR GH``` or ```make custom ARGS="5 F G 4 A D 1 W X B AB XS DF TR GH"```

Then in the terminal, enter your message using StdIn, and the encoded/decoded message will print. Enter ```q``` to quit the program.

### Homework and Presentation files
[Presentation](PRESENTATION.md)

[Homework](HOMEWORK.md)
