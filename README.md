# DeckOfCards
Goal of this project is to practice programming in Python by creating a Blackjack simulation. The simulation will allow for up to 7 players with a minimum of 2, including the dealer and be played with a deck of 52 cards. Making use of Object-Oriented Programming and working on the program's functionality and eventually integrate a UI to display actions such as each player's hand and input event handlers, etc. 

card_interface.py: holds the Card and Player object classes used for various types of card games
    - includes a class called Card which has a card's denomination and suit and a class called Player that has each player's hand, bet amount and balance
    - contains functions that simulate normal card game setup (i.e. shuffling a deck, betting, how many players)

main.py: contains the game Blackjack and its functionalities with implementations of real world moves
    - core functionality with functions that simulate Blackjack-specific plays such as the "hit" and "stand" actions

Cards folder: Snoopy Dog playing cards (credit to user on Flikr)