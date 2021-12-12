import random
import sys

HANGMANPICS = [
    '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
]


def game(file_name):
    with open(file_name) as file:
        words = [word.strip() for word in file.readlines()]

    word = random.choice(words)
    letters, guessed = list(word), set()

    for picture in HANGMANPICS:
        print("".join([letter if letter in guessed else '*' for letter in letters]))
        guessed.add(input("litera: "))

        if len(set(letters).difference(guessed)) == 0:
            print(f"{word}, OK!")
            exit()

        print(picture)


if __name__ == '__main__':
    assert len(sys.argv) == 2
    game(sys.argv[1])
