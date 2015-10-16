#!/usr/bin/env python
# encoding: utf-8

"""
GameOfWarV3.py

__author__ = "Daniel"

"""

import random	

def main():
	"""
	Deck, PlayerAHand and PlayerBHand are all lists
	"""
	
	Deck = []
	PlayerAHand = []
	PlayerBHand = []
	gameCounter = 0

	# Create deck.  Cards are represented by an integer value
	for i in range(52):
		Deck.append(i)
	
	# Shuffle the deck
	random.shuffle(Deck)
	
	# Deal 1/2 the cards to each player
	for i in range(26):
		PlayerAHand.append(Deck.pop())
		PlayerBHand.append(Deck.pop())
	
	# Main Gameplay
		
	while len(PlayerAHand) > 0 and len(PlayerBHand) > 0:
		gameCounter += 1
		PlayerAHand, PlayerBHand = playRound(PlayerAHand, PlayerBHand)
		if gameCounter > 1000:
			print("Draw")
			break
	# End of game
	
	print("There were ", gameCounter, " rounds played")
	
def playRound(PlayerA, PlayerB):
	aCard = PlayerA.pop()
	bCard = PlayerB.pop()
	aRank = getRank(aCard)
	bRank = getRank(bCard)
	if aRank > bRank:
		# A wins
		PlayerA.insert(0,aCard)
	elif aRank < bRank:
		# B wins
		PlayerB.insert(0,bCard)
	else:
		PlayerA, PlayerB = WAR(PlayerA,PlayerB)
	
	return PlayerA, PlayerB


def WAR(PlayerA, PlayerB):
	if len(PlayerA) > 5 and len(PlayerB) > 5:
		PlayerAHand = []
		PlayerBHand = []
		for d in range(5):
			PlayerAHand.append(PlayerA.pop())
			PlayerBHand.append(PlayerB.pop())
		if getRank(PlayerAHand[4]) > getRank(PlayerBHand[4]):
			PlayerA = PlayerAHand + PlayerBHand + PlayerA
		elif getRank(PlayerAHand[4]) < getRank(PlayerBHand[4]):
			PlayerA = PlayerAHand + PlayerBHand + PlayerB
		else:
			PlayerA, PlayerB = Loser(PlayerA, PlayerB)
	return PlayerA, PlayerB
	
def Loser(PlayerA, PlayerB):
	# Lose Cards
	return PlayerA, PlayerB

	
def getRank(anyCard):
	return anyCard % 13

if __name__ == '__main__':
	main()