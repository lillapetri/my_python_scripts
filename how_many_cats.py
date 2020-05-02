def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
            if userInput > 4:
                print('That\'s a lot of cats.')
            elif userInput <= 4:
                print('You have to buy more cats.')
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return userInput
            break


cats = inputNumber("How many cats do you have? ")