from game.wordle_game import WordleGame

def main():
    # new wordle game object
    wordle_game = WordleGame()

    # play as many rounds as player likes
    while True:
        wordle_game.play()
        inp = input('Play another round (y/n)? ')
        if inp.lower() != 'y':
            print('Goodbye.')
            break
        print()

if __name__ == '__main__':
    main()
