# Print first x terms of the series 3N + 2 which are not multiples of 4.

def number():
    while True:
        userInput = input('Please enter a non-negative integer number: ')
        if userInput.isnumeric():
            return int(userInput)
        else:
            print("Input error.")


def firstXTerms(x):
    n, i = 0, 1
    while n < x:
        term = 3 * i + 2
        if term % 4 != 0:
            print(term)
            n += 1
        i += 1


firstXTerms(number())
