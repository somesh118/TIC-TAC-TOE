board = [' ' for _ in range(9)]
def print_board():
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')
def is_game_over():
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != ' ':
            return True
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            return True
    if board[0] == board[4] == board[8] != ' ':
        return True
    if board[2] == board[4] == board[6] != ' ':
        return True
    if ' ' not in board:
        return True
    
    return False
def play_game():
    current_player = 'X'
    game_over = False

    while not game_over:
        print_board()
        move = input('Player ' + current_player + ', enter your move (0-8): ')

        if move.isdigit() and int(move) in range(9) and board[int(move)] == ' ':
            board[int(move)] = current_player
            game_over = is_game_over()
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'
        else:
            print('Invalid move. Try again.')

    print_board()

    if ' ' not in board:
        print("It's a tie!")
    else:
        winner = 'X' if current_player == 'O' else 'O'
        print('Player ' + winner + ' wins!')
play_game()

