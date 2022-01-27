## Boggle Game Solver

This project was made for CS470 Project 1: Boggle

The code in Boggle.py takes in a dictionary of words and a boggle board in a text file. The algorithm that I built goes through the entire board searching for possible words and then adding them to a list if it is a word.

Due to the amount of words that the algorithm checks for in such a small board I set a limit on the length that a word can be in order to make the code run a bit faster. To change this simply change the last value when calling the function findWords on line 258 to whatever you would like!
