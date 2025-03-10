# Tic Tac Toe Game

PYTHON = python3

all: run

run: 
	$(PYTHON) tic-tac-toe.py

clean:
	rm -rf __pycache__ 

