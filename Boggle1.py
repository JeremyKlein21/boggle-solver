# Jeremy Klein
# Boggle Phase 2

import time


# load board function to create the boggle board
def loadBoard(fileName):
    # creating global variables for the board as well as the number of columns and rows
    global myBoard, numRows, numCols, letters, inBoard, counter
    # opening and reading the text file containing the board
    inBoard = open(fileName, "r")
    inBoard = inBoard.read()
    # creating a list of just the letters
    letters = inBoard
    letters = letters.replace("\n", "")
    letters = letters.replace(" ", "")
    # setting intial values for the number of rows and columns
    numRows = 1
    numCols = 0

    # traversing through the board to get the number of columns and rows
    for _ in inBoard:
        if _ == "\n":
            numRows += 1

    # set cols = rows since it is a square board
    numCols = numRows

    # turning the board into a 2D array for future use
    myBoard = [[" "] * numCols for _ in range(numRows)]
    # creating indexs for the outer and inner loop and for the total number of letters
    outerIndex = 0
    innerIndex = 0
    totalIndex = 0
    # iterating through the rows and columns and assigning the letters to the 2D array
    while outerIndex < numRows:
        # setting the inner index to zero to loop through properly each time
        innerIndex = 0
        while innerIndex < numCols:
            myBoard[outerIndex][innerIndex] = letters[totalIndex]
            # incrementing the indexes
            innerIndex += 1
            totalIndex += 1
        outerIndex += 1

    # print that the board was loaded
    print()


# function that prints the board and takes in the board
def printBoard(tempBoard):
    # creating indexes to loop through the array and a temp prinot string
    outerIndex = 0
    innerIndex = 0
    tempString = "";

    # printing that this is what the current board looks like
    print("Current board: ")
    # while loops to traverse through the 2D array
    while outerIndex < numRows:
        # resetting the inner index for the columns and the tempstring for the new line of letters
        innerIndex = 0
        tempString = "";
        while innerIndex < numCols:
            # adding to temp string the letter and a space of the current index
            tempString += tempBoard[outerIndex][innerIndex]
            tempString += " "
            # incrementing the inner index
            innerIndex += 1
        # printing the line of letters followed by a new line
        print(tempString + "\n")
        # incrementing the outer index
        outerIndex += 1


# functioning for determining the next possible moves not considering a previous path
def possibleMoves(position):
    # creating an array of tuples to hold the coordinates of possible moves
    row = position[0]
    col = position[1]
    possibleMoves = []
    # checking the location and adding the possible moves accordingly
    if col == 0 and row == 0:
        possibleMoves.append((row, col + 1))
        possibleMoves.append((row + 1, col))
        possibleMoves.append((row + 1, col + 1))
    elif col == numCols - 1 and row == numRows - 1:
        possibleMoves.append((row - 1, col))
        possibleMoves.append((row, col - 1))
        possibleMoves.append((row - 1, col - 1))
    elif row == numRows - 1 and col == 0:
        possibleMoves.append((row - 1, col))
        possibleMoves.append((row - 1, col + 1))
        possibleMoves.append((row, col + 1))
    elif row == 0 and col == numCols - 1:
        possibleMoves.append((row, col - 1))
        possibleMoves.append((row + 1, col - 1))
        possibleMoves.append((row + 1, col))
    elif row == 0:
        possibleMoves.append((row, col - 1))
        possibleMoves.append((row + 1, col - 1))
        possibleMoves.append((row + 1, col))
        possibleMoves.append((row + 1, col + 1))
        possibleMoves.append((row, col + 1))
    elif col == 0:
        possibleMoves.append((row - 1, col))
        possibleMoves.append((row - 1, col + 1))
        possibleMoves.append((row, col + 1))
        possibleMoves.append((row + 1, col + 1))
        possibleMoves.append((row + 1, col))
    elif row == numRows - 1:
        possibleMoves.append((row, col - 1))
        possibleMoves.append((row - 1, col - 1))
        possibleMoves.append((row - 1, col))
        possibleMoves.append((row - 1, col + 1))
        possibleMoves.append((row, col + 1))
    elif col == numCols - 1:
        possibleMoves.append((row - 1, col))
        possibleMoves.append((row - 1, col - 1))
        possibleMoves.append((row, col - 1))
        possibleMoves.append((row + 1, col - 1))
        possibleMoves.append((row + 1, col))
    else:
        possibleMoves.append((row, col - 1))
        possibleMoves.append((row - 1, col - 1))
        possibleMoves.append((row - 1, col))
        possibleMoves.append((row - 1, col + 1))
        possibleMoves.append((row, col + 1))
        possibleMoves.append((row + 1, col + 1))
        possibleMoves.append((row + 1, col))
        possibleMoves.append((row + 1, col - 1))

    # printing the list of possible moves from the given spot
    return possibleMoves


# printing the legal moves given a path
def legalMoves(possibleMoves, path):
    # creating indexes to traverse through the path and poussible moves lists
    pathIndex = 0
    pmIndex = 0
    # creating a temporary return variable
    legalMoves = possibleMoves.copy()
    # print("legalMoves(", possibleMoves,", ",path,"): ", legalMoves)
    # print("len(path): ", len(path))

    # traversing through the path list and legal moves list
    while pathIndex < len(path):
        # resetting the possible moves index to traverse through the list each time
        pmIndex = 0
        while pmIndex < len(legalMoves):
            # checking if the possible move was already apart of a path
            if path[pathIndex] == legalMoves[pmIndex]:
                # removing the move if it was in the path
                legalMoves.pop(pmIndex)
            # incrementing the indexes
            pmIndex += 1
        pathIndex += 1
    # returning the list of legal moves
    return legalMoves


# determine whether the word made from the path is an actual word
def examineState(board, currentCoord, path):
    # creating a variable to hold the word created
    testWord = ""
    # value for whether or not it is a word
    isWordBool = False
    # tuple being returned with the yes or no and word
    returnTuple = (" ", " ")
    # setting the index to the length so it creates the word the right way
    pathIndex = 0
    # traversing through the path
    while pathIndex < len(path):
        # adding the letter to the word being tested
        testWord += board[path[pathIndex][0]][path[pathIndex][1]]
        # decrementing the index
        pathIndex += 1

    # adding the current coordinate the player is on to the word
    testWord += board[currentCoord[0]][currentCoord[1]]

    # function call to check if the word is in the dictionary
    isWordBool = isWord(testWord)

    # checking if the word boolean value is true and creating the return tuple accordingly
    if isWordBool == True:
        returnTuple = ("Yes", testWord)
    else:
        returnTuple = ("No", testWord)

    # returning the tuple created
    return returnTuple


# function to check if a word is in the dictionary
def isWord(word):
    # setting the word to lowercase in order to compare to the possible words
    word = word.lower()
    # opening and stripping the text file of new line characters
    words = open('possiblewords.txt', "r")
    words = words.read().strip().split('\n')
    # creating an index to loop through the dictionary
    index = 0

    # traversing through the dictionary of words
    while index < len(words):
        # checking if the word we created is any word in the dictionary
        if word == words[index]:
            # returning true if it is
            return True
        # incrementing the index
        index += 1

    # returning false if it is not a real word
    return False


# initializing global variable to count the number of moves
counter = 0


# function to find all the possible words on the board
def findWords(board, positions, currentPath, foundWords, depth):
    # calling global variable counter to increment
    global counter
    counter += 1
    # for loop to start from each letter on the board
    for currentMove in positions:
        # deconstructing the tuple
        (foundWord, word) = examineState(board, currentMove, currentPath)
        # checking if the current word is in the dictionary
        if foundWord == "Yes":
            # appending it to the list of words
            foundWords.append(word)
        # creating a new path variable and adding the most recent corrdinates
        newPath = currentPath.copy()
        newPath.append(currentMove)
        # calling legal moves to get the moves that can be made
        legalMovesToSearch = legalMoves(possibleMoves(currentMove), newPath)
        # recursive call if there are still moves to make and limiting the length of the words found
        if len(legalMovesToSearch) > 0 and depth > 0:
            findWords(board, legalMovesToSearch, newPath, foundWords, depth - 1)


# helper function to start the search
def searchBoard(board):
    # creating an array of 2d coordinates
    startingLocations = []
    for row in range(numRows):
        for col in range(numCols):
            # adding the coordinate to the list
            startingLocations.append((row, col))
    # creating an array for the found words
    foundWords = []
    # calling find words
    findWords(board, startingLocations, [], foundWords, 3)
    # returning the parameter that was used in recursion
    return foundWords


# main function to run the program
def main():
    # printing that the program is running
    print()
    print("OUTPUT FROM RUNNING THE PROGRAM: ")
    # loading the board
    loadBoard("fourboard.txt")
    # printing the board to the user
    printBoard(myBoard)
    # printing that the program is now running
    print("And we're off!\nRunning with cleverness OFF")
    # starting the timer
    start = time.time()
    # calling search board and sotring the array of words
    foundWords = searchBoard(myBoard)
    # stopping the timer
    end = time.time()
    # creating a variable for the total elapsed time
    elapsed = end - start
    # printing the amount of searches in the amount of time
    print("All done\n\nSearched total of ", counter, " moves in ", elapsed, " seconds")
    # printing the words based on their length in arrrays
    print("\nWords found:")
    # for loop to go through the different lengths of words
    for length in range(1, 4):
        # creating a list of fitered words based on the length and printing it 
        wordsOfLength = list(filter(lambda word: len(word) == length, foundWords))
        if len(wordsOfLength) > 0:
            print(length, "-letter words: ", wordsOfLength)
    # printing the total amount of words found
    print("\nFound ", len(foundWords), " words in total.")
    # printing the alphabetized array of words
    print("Alpha-sorted words in total:")
    print(sorted(foundWords))
