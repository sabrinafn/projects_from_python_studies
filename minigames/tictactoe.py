import os

def display_game(game_matrix):
    print("   Tic Tac Toe   ")
    count = 0
    for row in game_matrix:
        print("  {}  |  {}  |  {} ".format(*row[0], *row[1], *row[2]))
        if count < 2:
            print("-----|-----|-----")
        count += 1

def get_available_positions_in_matrix(choice_list, flat_matrix):
    for index in range (len(flat_matrix)):
        if flat_matrix[index] == 'O' or flat_matrix[index] == 'X':
            choice_list[index] = '*'

    return choice_list


def position_choice(game_matrix,current_player):
    choice = 'wrong'
    choice_list = ['1','2','3','4','5','6','7','8','9']
    flat_matrix = sum(game_matrix, [])
    updated_list = get_available_positions_in_matrix(choice_list, flat_matrix)

    while choice not in updated_list:
        result = input("Player {}: Pick a free position from 1 to 9: ".format(current_player))

        if result not in choice_list:
            print("Sorry, invalid choice!")
        else:
            choice = result

    return int(choice)

def replacement_choice(game_matrix, position, character):
    if position in range(1,4):
        x = 0
        position = position - 1
    elif position in range(4,7):
        x = 1
        position = position - 4
    else:
        x = 2
        position = position - 7

    game_matrix[x][position] = character

    return game_matrix

def position_empty(current_char):
    if current_char == ' ':
        return True
    return False

def at_least_three(game_matrix):
    count = {'x': 0, 'o': 0}
    for row in game_matrix:
        for char in row:
            if char == 'X':
                count['x'] += 1
            if char == 'O':
                count['o'] += 1
    if count['x'] >= 3 or count['o'] >= 3:
        return True
    return False

def win_in_rows(game_matrix):
    for row in game_matrix:
        if not position_empty(row[0]) and not position_empty(row[1]) and not position_empty(row[2]):
            if row[0] == row[1] == row[2]:
                return True
    return False

def win_in_columns(game_matrix):
    myrange = range(0,3)
    col = 0

    for row in myrange:
        if not position_empty(game_matrix[col][row]) and not position_empty(game_matrix[col + 1][row]) and not position_empty(game_matrix[col + 2][row]):
            if game_matrix[col][row] == game_matrix[col + 1][row] == game_matrix[col + 2][row]:
                return True

    return False

def diagonal_win(game_matrix):
    pass
    # left to right
    if not position_empty(game_matrix[0][0]) and not position_empty(game_matrix[1][1]) and not position_empty(game_matrix[2][2]):
        if game_matrix[0][0] == game_matrix[1][1] == game_matrix[2][2]:
            return True

    # right to left
    if not position_empty(game_matrix[0][2]) and not position_empty(game_matrix[1][1]) and not position_empty(game_matrix[2][0]):
            if game_matrix[0][2] == game_matrix[1][1] == game_matrix[2][0]:
                return True
    
    return False

def gameon_choice():
    choice = 'wrong'

    while choice not in ['Y','N']:
        choice = input("Keep playing? (Y or N) ")
        if choice not in ['Y','N']:
            print("Sorry, I don't understand! ")
    if choice == 'Y':
        return True
    return False

def character_choice(players):
    # players = {'1':['1','*'], '2':['2','*']}
    choice = 'wrong'

    while choice not in ['X','O']:
        choice = input("Which character would you like to be? ('X' or 'O') ")

        if choice not in ['X','O']:
            print("Sorry, I don't understand! ")

    if choice == 'X':
        players['1'][1] = 'X'
        players['2'][1] = 'O'
        return players
    elif choice == 'O':
        players['1'][1] = 'O'
        players['2'][1] = 'X'
        return players
    return False

def win(game_matrix):
    # checks rows
    if win_in_rows(game_matrix):
        return True
    
    # check columns
    if win_in_columns(game_matrix):
        return True

    # check diagonal
    if diagonal_win(game_matrix):
        return True

    return False


def tie(game_matrix):
    flat_matrix = sum(game_matrix, [])

    for char in flat_matrix:
        if position_empty(char):
            return False

    return True

def gameover(game_matrix,current_player):
    if not at_least_three(game_matrix):
        return True
    
    if win(game_matrix):
        os.system('clear')
        print('     Game over     ')
        display_game(game_matrix)
        if current_player == '1':
            other_player = '2'
        else:
            other_player = '1'
        print('Player {} is the winner!'.format(current_player))
        print('Player {} lost!'.format(other_player))
        return False
    elif tie(game_matrix):
        os.system('clear')
        print('     Game over     ')
        display_game(game_matrix)
        print('        Tie        ')
        return False

    return True


game_on = True
game_matrix = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
players = {'1':['1','*'], '2':['2','*']}
current_player = players['1']

while game_on:
    if players['1'][1] == '*' and players['2'][1] == '*':
        players = character_choice(players)
    else:
        if current_player[0] == '1':
            current_player = players['2']
        else:
            current_player = players['1']

    display_game(game_matrix)
    position = position_choice(game_matrix,current_player[0])
    game_matrix = replacement_choice(game_matrix,position,current_player[1])
    os.system('clear')
    game_on = gameover(game_matrix,current_player[0])
    if not game_on:
        play_again = gameon_choice()
        if play_again:
            game_matrix = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
            game_on = play_again
        os.system('clear')


    


