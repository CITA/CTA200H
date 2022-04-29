def main():

    import numpy

    secret = numpy.random.permutation(range(10))[:4]

    print('welcome to Bullseye')

    game_on = True
    while game_on:
        raw_guess = str(input('Enter guess (4 digits, e.g. 1234)\n'))
        print('raw guess '+raw_guess)
        assert(len(raw_guess)==4)
        guess = [int(digit) for digit in raw_guess]
        assert(len(set(guess))==4)

        # Grading
        bulleyes = 0
        hits = 0
        for n, digit in enumerate(guess):
            if digit == secret[n]:
                bulleyes += 1
            elif digit in secret:
                hits += 1
        if bulleyes == 4:
            print('You win!\n')
            game_on = False
        else:
            print(str(bulleyes)+' bulleyes and '+str(hits)+' hits\n')

if __name__ == '__main__':

    main()
    
