#coding utf-8


# definitions

number_rows_columns = 9



score_to_win = 3

player_a_wins = ["X", "X", "X"]
player_b_wins = ["O", "O", "O"]

player_id = {"A": "X", "B":"O"}


matrix = [["?", "?", "?"],
          ["?", "?", "?"],
          ["?", "?", "?"]]

indic = range(len(matrix))


# actual code


def winner_checker():
    aux = []
    lines = []
    columns = []
    diagonals = []


    def checker(a_list):
        if a_list == player_a_wins:
            print(9*"\t", "PLAYER A WINS")
            quit()
        elif a_list == player_b_wins:
            print(9*"\t", "PLAYER B WINS")
            quit()
        else:
            del (a_list[0:len(a_list)])


    # checking lines

    for line in indic:
        for column in range(len(matrix)):
            lines.append(matrix[line][column])

        checker(lines)


    # checking columns

    for lines in indic:
        for column in indic:
            columns.append(matrix[column][lines])

        checker(columns)


    #checking diagonals

    for lines in indic:
        diagonals.append(matrix[lines][lines])

    checker(diagonals)


    for lines in indic:
        for across in indic:
            diagonals.append(matrix[lines][across])
    aux.append(diagonals[2:7:2])
    diagonals = aux[0]

    checker(diagonals)


def matrix_display():
    print("\n")
    for i in indic:
        print(9*"\t", matrix[i], "\n")


def get_play(player):
    print("\n\nPlayer", player)
    row = int(input("type the row position: "))
    column = int(input("type the column position: "))

    if row > 3 or column > 3 or row < 1 or column < 1:
        this_player = player
        print("\nInvalid position, type row and column values between 0 and 3.")
        this_position = get_play(this_player)
        return this_position
    elif matrix[row-1][column-1] == "X" or matrix[row-1][column-1] == "O":
        this_player = player
        print("\nTaken position, type a combination [row, column] that hasn't been used yet.")
        this_position = get_play(this_player)
        return this_position
    else:
        position = (row-1, column-1)
        return position


def start():
    matrix_display()
    for n in range(number_rows_columns):
        if n%2 == 0: # this means that it's player A's turn
            play = get_play("A")
            matrix[play[0]][play[1]] = "X"
        else:
            play = get_play("B")
            matrix[play[0]][play[1]] = "O"

        matrix_display()
        winner_checker()

start()
