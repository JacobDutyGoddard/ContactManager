# Library functions commonly used

def gatherNumberInput(prompt="Enter a number {FALLBACK}: "): # Author: Jacob Duty
    # This function accepts one argument, prompt
    # It will call for the users input repeatedly, with the selected prompt
    # It will validate the input until its strictly an integer.
    while True:
        try:
            num = int(input(prompt))
            if num > 0:
                return num
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")