import sys

def make_array():
    with open(sys.argv[1], 'r') as file:
        lines = file.readlines()
    input_array = [list(line.strip()) for line in lines]
    two_d_array = [[char for char in row] for row in input_array]
    return two_d_array

def search_for_numbers(array, row, col, visited):
    if row < 0 or row >= len(array) or col < 0 or col >= len(array[0]) or tuple([row, col]) in visited or not array[row][col].isdigit():
        return 0
    c = col+1
    num = int(array[row][col])
    offset = 0
    while c < len(array[0]) and array[row][c].isdigit():
        if tuple([row, c]) in visited:
            return 0
        visited.add(tuple([row, c]))
        num *=10
        num+= int(array[row][c])
        c+=1
        offset += 1
        
    c = col -1

    while c >= 0 and array[row][c].isdigit():
        if tuple([row, c]) in visited:
            return 0
        visited.add(tuple([row, c]))
        leftnum = int(array[row][c])
        for i in range((col-c) + offset):
            leftnum *= 10
        num += leftnum
        c -= 1

    return num

def search_for_gears(array, row, col, visited):
    if row < 0 or row >= len(array) or col < 0 or col >= len(array[0]) or tuple([row, col]) in visited or not array[row][col].isdigit():
        return 0
    c = col+1
    num = int(array[row][col])
    offset = 0
    while c < len(array[0]) and array[row][c].isdigit():
        if tuple([row, c]) in visited:
            return 0
        visited.add(tuple([row, c]))
        num *=10
        num+= int(array[row][c])
        c+=1
        offset += 1
        
    c = col -1

    while c >= 0 and array[row][c].isdigit():
        if tuple([row, c]) in visited:
            return 0
        visited.add(tuple([row, c]))
        leftnum = int(array[row][c])
        for i in range((col-c) + offset):
            leftnum *= 10
        num += leftnum
        c -= 1

    return num

count = 0
input = make_array()
visited = set()
gearsvisited = set()
gearRatio = 0
for row in range(len(input)):
    for col in range(len(input[0])):
        current_char = input[row][col]
        if current_char != '.' and not current_char.isdigit():
            gearCount = 0
            currGearRatio = 0
            if current_char == '*':
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        addedNum = search_for_gears(input, row + i, col + j, gearsvisited)
                        if addedNum != 0:
                            if gearCount == 0:
                                currGearRatio = addedNum
                            if gearCount == 1:
                                currGearRatio *= addedNum
                            gearCount += 1
                if gearCount == 2:
                    gearRatio += currGearRatio
            for i in range(-1, 2):
                for j in range(-1, 2):
                    addedNum = search_for_numbers(input, row + i, col + j, visited)
                    count += addedNum       
print("Total Count = " + str(count))  
print("Total sum of gear ratio products = " + str(gearRatio))