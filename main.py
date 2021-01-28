lines = "_________"
numbers = "0123456789"

#for git
def line_to_table(line):
    pattern = "".join([x + " " for x in line])
    print("---------")
    print(f'| {pattern[:5]} |')
    print(f'| {pattern[6:11]} |')
    print(f'| {pattern[12:]}|')
    print("---------")


def analys(str):
    lst = []
    lst.append(str[:3])
    lst.append(str[3:6])
    lst.append(str[6:])
    lst.append(str[0] + str[3] + str[6])
    lst.append(str[1] + str[4] + str[7])
    lst.append(str[2] + str[5] + str[8])
    lst.append(str[0] + str[4] + str[8])
    lst.append(str[2] + str[4] + str[6])


    count_x = 0
    count_o = 0
    for elem in lst:
        if elem == "XXX":
            count_x += 1
        elif elem == "OOO":
            count_o += 1

    if (abs(str.count("X") - str.count("O")) >= 2) or (count_o + count_x >= 2):
        return "Impossible"
    elif str.count("_") == 0 and count_x == 0 and count_o == 0:
        return "Draw"
    elif str.count("_") != 0 and count_x == 0 and count_o == 0:
        return "Game not finished"
    elif count_x != 0:
        return "X wins"
    elif count_o != 0:
        return "O wins"


line_to_table(lines)
count = True

while True:
    cor = input("Enter the coordinates:").split()
    if (cor[0] not in numbers) or (cor[1] not in numbers):
        print("You should enter numbers!")
        continue
    cor = [int(x) - 1 for x in cor]
    if (cor[0] > 2) or (cor[1] > 2):
        print("Coordinates should be from 1 to 3!")
        continue
    elif (cor[0] < 0) or (cor[1] < 0):
        print("Coordinates should be from 1 to 3!")
        continue
    index = (cor[0]) * 3 + cor[1]
    if lines[index] == "_":
        matrix = list(lines)
        if count:
            matrix[index] = "X"
        if not count:
            matrix[index] = "O"
        lines = "".join(matrix)
        line_to_table(lines)
        result = analys(lines)
        if (result == "Draw") or (result == "X wins") or (result == "O wins") or (result == "Impossible"):
            print(result)
            break
        count = not count
        continue
    else:
        print("This cell is occupied! Choose another one!")
        continue
