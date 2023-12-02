def display_grid(seq):
    print('---------')

    # first line
    print('| ', end='')
    print(' '.join(seq[:3]), end='')
    print(' |')
    # second line
    print('| ', end='')
    print(' '.join(seq[3:6]), end='')
    print(' |')
    # third line
    print('| ', end='')
    print(' '.join(seq[6:9]), end='')
    print(' |')

    print('---------')


def count_symbol(matrix, s):
    count = 0
    for line in matrix:
        for symbol in line:
            if symbol == s:
                count += 1
    return count


def check_row(matrix, row):
    if matrix[row][0] == matrix[row][1] == matrix[row][2] and matrix[row][0] != '_':
        return matrix[row][0]
    return False


def check_column(matrix, col):
    if matrix[0][col] == matrix[1][col] == matrix[2][col] and matrix[0][col] != '_':
        return matrix[0][col]
    return False


def check_diagonals(matrix):
    if matrix[0][0] == matrix[1][1] == matrix[2][2] and matrix[0][0] != '_':
        return matrix[0][0]
    if matrix[0][2] == matrix[1][1] == matrix[2][0] and matrix[0][2] != '_':
        return matrix[0][2]
    return False


def get_game_state(matrix):
    # more symbols of one type than the other
    if abs(count_symbol(matrix, 'X') - count_symbol(matrix, 'O')) > 1:
        return 'Impossible'
    winner = ''
    # determine winner from diagonals early since only one can be winning from diagonals
    if check_diagonals(matrix):
        if winner == '':
            winner = check_diagonals(matrix)
        else:
            return 'Impossible'

    # determine the winner from rows and columns
    for i in range(0, len(matrix)):
        if check_row(matrix, i):
            if winner == '':
                winner = check_row(matrix, i)
            else:
                return 'Impossible'
        if check_column(matrix, i):
            if winner == '':
                winner = check_column(matrix, i)
            else:
                return 'Impossible'

    if winner == '':
        for line in matrix:
            if '_' in line:
                return 'Game not finished'
        return 'Draw'
    return winner + ' wins'


def main():
    empty_grid = "_________"
    res = empty_grid
    current = 'X'
    matrix = [list(empty_grid[i:i + 3]) for i in range(0, len(res), 3)]
    display_grid(res.replace('_', ' '))

    while True:
        if get_game_state(matrix).find('wins') > 0:
            print(get_game_state(matrix))
            break
        if get_game_state(matrix) == 'Draw':
            print('Draw')
            break

        try:
            coordinates = input().split()
            if len(coordinates) == 1:
                print("Not enough coordinates")
                continue
            x = int(coordinates[0])
            y = int(coordinates[1])
        except ValueError:
            print('You should enter numbers!')
            continue
        if x > 3 or y > 3 or x < 1 or y < 1:
            print('Coordinates should be from 1 to 3!')
            continue
        if matrix[x - 1][y - 1] == 'X' or matrix[x - 1][y - 1] == 'O':
            print('This cell is occupied! Choose another one!')
            continue
            
        matrix[x - 1][y - 1] = current

        if current == 'X':
            current = 'O'
        else:
            current = 'X'

        res = ''.join([''.join([str(ele) for ele in sub]) for sub in matrix])
        display_grid(res.replace('_', ' '))


main()
