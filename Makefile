default: app/enigma_m3.py
	@python3 app/enigma_m3.py 1 A A 2 A A 3 A A C

custom: app/enigma_m3.py
	@python3 app/enigma_m3.py $(ARGS)
