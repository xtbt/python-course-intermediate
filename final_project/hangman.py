from random import randint
import os


def draw_header():
    header = '''
        *******************************************************************************
        **************************** THE HANGMAN GAME *********************************
        ****************** DEVELOPER: JONATHAN SANCHEZ LUNA (JSL_CODE) ****************
        *******************************************************************************

        '''
    print(header)


def draw_body(players_name: str, chances: int) -> bool:
    title = '''
        WELCOME: {players_name}                                     CHANCES: {chances}
    '''.format(players_name=players_name, chances=chances)
    print(title)

    hangman = ['','','','','','','','']
    hangman[0] = '''
                                __________________________
                                            |
                                           _|_
                                          (x_x)
                                           /|\\
                                          | | |
                                         _| | |_
                                           / \\
                                          |   |
                                         _|   |_
    '''
    hangman[1] = '''
                                __________________________

                                           ___
                                          (^.^)
                                           /|\\
                                          | | |
                                         _| | |_
                                           / \\
                                          |   |
                                         _|   |_
    '''
    hangman[2] = '''
                                __________________________

                                           ___
                                          (^.^)
                                           /|\\
                                          | | |
                                         _| | |_
                                           /
                                          |
                                         _|
    '''
    hangman[3] = '''
                                __________________________

                                           ___
                                          (^.^)
                                           /|\\
                                          | | |
                                         _| | |_



    '''
    hangman[4] = '''
                                __________________________

                                           ___
                                          (^.^)
                                           /|
                                          | |
                                         _| |



    '''
    hangman[5] = '''
                                __________________________

                                           ___
                                          (^.^)
                                            |
                                            |
                                            |



    '''
    hangman[6] = '''
                                __________________________

                                           ___
                                          (^.^)






    '''
    hangman[7] = '''
                                __________________________









    '''
    print(hangman[chances])
    return chances > 0


def draw_word(random_word: list, round_status: bool):
    pass


def display_letter_message():
    print('***** ONLY LETTERS ARE ALLOWED!!! *****')


def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


def get_random_word() -> list:
    random_word = [] # Random word to return
    category_words = [] # Read words from file
    categories = ['videogames', 'movies', 'technology']
    selected_category_index = randint(0, len(categories) - 1)
    selected_category = categories[selected_category_index]
    with open(selected_category+'.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.replace('\n', '')
            category_words.append(line)
    selected_word_index = randint(0, len(category_words) - 1)
    selected_word = category_words[selected_word_index]
    random_word.append(selected_category+','+selected_word)
    return random_word


def get_scores() -> dict:
    scores = {}
    with open('scores.txt', 'r', encoding='utf-8') as f:
        scores = {str(line.replace('\n', '').split(',')[0]): int(line.replace('\n', '').split(',')[1]) for line in f if line[0] and line[1]}
    return scores


def score_save(players_name: str, players_score: int) -> bool:
    score_list = get_scores()
    with open('records.txt', 'w', encoding='utf-8') as f:
        for line in f:
            pass
            # f.write(name)
            # f.write('\n')


def main():
    players_name = input('Enter your name or alias: ') # For score
    continue_playing = 'yes'
    while continue_playing.lower() == 'yes':
        random_word = get_random_word()
        chances = 7 # At the start the chances are 7
        letter_message = False
        while chances > 0:
            clear_screen()
            draw_header()
            round_status = draw_body(players_name, chances)
            draw_word(random_word, round_status)
            if letter_message:
                display_letter_message()
                letter_message = False
            letter = input('Enter a letter: ')
            if len(letter) != 1:
                letter_message = True


if __name__ == '__main__':
    main()