nameList = ["James", "Cindy", "Pierce", "Jay"] # List
name = input("What is your name? ") # User input
def addName(name): # Procedure
    for name in nameList: # Iteration
        if isinstance(name, str) == True: # Selection
            nameList.append(name) # Required to get the point for iteration
            print(name) # This line is actually needed to make user input visible
addName(name) # Procedure must be called at least once
