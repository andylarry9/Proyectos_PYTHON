

###PROYECTO Tic-Tac-Toe del ITB


import random

# Inicializa el tablero de juego
board = [str(i) for i in range(1, 10)]

# Función para imprimir el tablero
def print_board():
    print("+-------+-------+-------+")
    for i in range(3):
        print("|       |       |       |")
        print(f"|   {board[3 * i]}   |   {board[3 * i + 1]}   |   {board[3 * i + 2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

# Función para verificar si alguien ha ganado
def check_winner(player):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Función para verificar si el tablero está lleno
def is_board_full():
    return all(cell in ['X', 'O'] for cell in board)

# Función principal para el juego
def play_game():
    print("¡Bienvenido al Tic-Tac-Toe!")
    print_board()

    # Primer movimiento de la máquina
    board[4] = 'X'
    print("\nLa máquina juega 'X' en el centro del tablero:")
    print_board()

    while True:
        # Movimiento del usuario
        user_move = input("Introduce el número del cuadro donde deseas poner tu 'O': ")
        if user_move not in [str(i) for i in range(1, 10)]:
            print("Entrada inválida. Por favor, introduce un número entre 1 y 9.")
            continue

        user_move = int(user_move) - 1

        if board[user_move] in ['X', 'O']:
            print("Ese cuadro ya está ocupado. Elige otro.")
            continue

        board[user_move] = 'O'
        print("\nTu movimiento:")
        print_board()

        # Verificar si el usuario ganó
        if check_winner('O'):
            print("¡Felicidades, has ganado!")
            break

        # Verificar si el tablero está lleno
        if is_board_full():
            print("El juego termina en empate.")
            break

        # Movimiento de la máquina
        while True:
            machine_move = random.randint(0, 8)
            if board[machine_move] not in ['X', 'O']:
                board[machine_move] = 'X'
                print("\nLa máquina juega:")
                print_board()
                break

        # Verificar si la máquina ganó
        if check_winner('X'):
            print("La máquina gana. ¡Suerte la próxima vez!")
            break

        # Verificar si el tablero está lleno
        if is_board_full():
            print("El juego termina en empate.")
            break

# Ejecuta el juego
play_game()



    














