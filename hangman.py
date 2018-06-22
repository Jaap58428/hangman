# The game Hangman
# Author: Jaap Kanbier


def start_game():
    print('\n'
          'Welcome to HANGMAN! \n'
          '\n'
          'This program will test your mental power to guess letters. \n'
          'Let\'s start. Would you like a easy, medium or hard game? \n'
          '\n'
          '(1) EASY - 4 letter word \n'
          '(2) MEDIUM - 5 or 6 letter word \n'
          '(3) HARD - 7 letter word \n'
          '(4) INSANE - 8 letter word! Wow, you are brave O_o \n')


def take_difficulty():
    difficulty = input('\n'
                       'Please enter 1, 2, 3 or if you dare 4... \n'
                       '\n'
                       'Your choice: ')

    return difficulty if valid_difficulty(difficulty) else take_difficulty()


def valid_difficulty(user_difficulty):
    return int(user_difficulty) in range(1,5)


def pick_word(user_difficulty):
    if user_difficulty == '1':
        file_prefix = 'easy'
    elif user_difficulty == '2':
        file_prefix = 'medium'
    elif user_difficulty == '3':
        file_prefix = 'hard'
    elif user_difficulty == '4':
        file_prefix = 'insane'
    else:
        return None

    file_name = file_prefix + '_words.txt'

    with open(file_name, 'r') as word_data:
        word_list = word_data.read().splitlines()

    import random
    return random.choice(word_list)


def visualize_progress(wrong_guesses):
    layer_1 = '________'
    layer_2 = '|      |'
    wrong_0 = '|'
    wrong_1 = '|      O'     # head
    wrong_2 = '|      |'     # body without arms
    wrong_3 = '|     /'      # left leg
    wrong_4 = '|     / \ '   # right leg
    wrong_5 = '|     -|'     # left arm
    wrong_6 = '|     -|-'    # right arm
    layer_3 = '--------'

    print(layer_1)
    print(layer_2)

    if wrong_guesses >= 1:
        print(wrong_1)
    else:
        print(wrong_0)

    if wrong_guesses == 6:
        print(wrong_6)
    elif wrong_guesses == 5:
        print(wrong_5)
    elif wrong_guesses >= 2:
        print(wrong_2)
    else:
        print(wrong_0)

    if wrong_guesses >= 4:
        print(wrong_4)
    elif wrong_guesses >= 3:
        print(wrong_4)
    else:
        print(wrong_0)

    print(wrong_0)
    print(layer_3)


def get_wrong_guess_count(secret_word, guesses):

    wrong_guess_count = 0
    for guess in guesses:
        wrong_guess_count += 1 if guess not in secret_word else False

    return wrong_guess_count


def get_guesses(secret_word, guesses):
    result = ''

    for letter in secret_word:
        if letter in guesses:
            result += letter
        else:
            result += '_'

    return result


def you_lost(secret_word):
    print('Sadly you couldn\'t guess the word:')
    print(secret_word.upper())
    play_again()


def you_won(secret_word):
    print('Hurray!!! You guessed the word:')
    print(secret_word.upper())
    play_again()


def play_again():
    print('Would you like to play again?')
    user_input = input('Y/N: ').upper()

    if user_input == 'Y':
        main()
    elif user_input == 'N':
        return
    else:
        play_again()


def get_wrong_guesses(secret_word, guesses):
    results = []
    for guess in guesses:
        results.append(guess) if guess not in secret_word else False

    return results


def take_letter(guesses):
    next_guess = input('\nYour next guess: ')

    if next_guess in guesses:
        print('\nYou already tried', next_guess.upper())
    else:
        guesses.append(next_guess)
    return guesses


def make_guess(secret_word, guesses):
    wrong_guess_count = get_wrong_guess_count(secret_word, guesses)

    # check for winner/loser
    if wrong_guess_count > 6:
        you_lost(secret_word)
        return
    elif secret_word == get_guesses(secret_word, guesses):
        you_won(secret_word)
        return

    visualize_progress(wrong_guess_count)

    print('\nYou made', wrong_guess_count, 'mistakes so far:')
    wrong_guesses = get_wrong_guesses(secret_word, guesses)
    print(' '.join(wrong_guesses).upper())

    print('\nYour progress:')
    print(' '.join(get_guesses(secret_word, guesses).upper()))

    guesses = take_letter(guesses)

    make_guess(secret_word, guesses)


def main():
    start_game()
    difficulty = take_difficulty()
    secret_word = pick_word(difficulty)

    make_guess(secret_word, [])


if __name__ == '__main__':
    main()
