#ПК играет в крестики-нолики против человека

# Глобальные константы
X = "X"
O = "O"
EMPTY = " "
TIE = "Ничья"
NUM_SQUADES = 9

def display_instruct():
    """Выводит на экран инструкцию для игрока. """
    print(
    """
    Добро пожаловать на ринг грандиознейших состязаний
    всех времен! Твой мозг и мой процеессор сойдутся
    в схватке за доской игры!
    Чтобы сделать ход, введи число от 0 до 8. Числа 
    соответсвутют полям доски - так, как показано ниже:
    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8
    Приготовься к бою!
    """
    )
def ask_yes_no(question):
    """Задает вопрос да или нет"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
        return response
    
def ask_number(question, low, high):
    """Просит ввести число из диапазона"""
    response = None
    while response not in range(low,high):
        response = int(input(question))
    return question

def pieces():
    """Определяет принадлежгность первого хода"""
    go_first = ask_yes_no("Хочешь первый ход? y/n: ")
    if go_first == "y":
        print("Окей, ходи первый")
        human = X 
        computer = O
    else:
        print("Тогда буду начинать я")
        computer = X
        human = O
    return computer, human

def new_board():
    """Создает новую игровую доску"""
    board = []
    for square in range(NUM_SQUADES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Отображает игровую доску на экране"""
    print(f"\n\t {board[0]} | {board[1]} | {board[2]}")
    print("\t ---------")
    print(f"\n\t {board[3]} | {board[4]} | {board[5]}")
    print("\t ---------")    
    print(f"\n\t {board[6]} | {board[7]} | {board[8]} \n")

def legal_moves(board):
    """Cоздает список доступных ходов"""
    moves = []
    for square in range(NUM_SQUADES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    """Определяет победителя игры"""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None

def human_move(board, human):
    """Получает ход человека"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход. Выбери одно из полей 0-8 ", O, NUM_SQUADES)
        if move not in legal:
            print("Это поле уже занято!\n")
    print("Ладно..")
    return move

def computer_move(board, computer, human):
    """Ход компьютерного противника"""
    # Создаем копию доски
    board = board [:]
    # Поля от лучшего к худшему
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Я выберу поле номер", end="")
    for move in legal_moves(board):
        board[move] = computer
    # если следующим ходом может победить ПК, выберем это
        if winner(board) == computer:
            print(move)
            return move 
    # выполнив проверку, отменим внесенные изменения
        board[move] = EMPTY
    for move in legal_moves(board):
        board[move] = human
    # если следующим ходом может победить человек, блокируем этот ход
        if winner(board) == human:
            print(move)
            return move
    # выполнив проверку, отменим внесенные изменения
        board[move] = EMPTY

    # поскольку следующим ходом ни одна сторона не сможет победить
    # выберем лучшее из доступных полей
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
        
def next_turn(turn):
    """Осуществляет переход хода"""
    if turn == X:
        return O
    else:
        return X
    
def congart_winner(the_winner, computer, human):
    """Поздравляет победителя игры"""
    if the_winner != TIE:
        print(f"Три {the_winner} в ряд!")
    else:
        print("Ничья!\n")
    if the_winner == computer:
        print("ПК победил")
    elif the_winner == human:
        print("Поздравляю, ты победил!")
    elif the_winner == TIE:
        print("Нам повезло, ничья")

def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congart_winner(the_winner, computer, human)


    # ЗАПУСК ПРОГРАММЫ
main()
input("\n\nPress Enter to exit")


