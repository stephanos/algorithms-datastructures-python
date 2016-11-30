def sort(list):
    for index in range(1, len(list)):
        curr = list[index]
        position = index

        while position > 0 and list[position-1] > curr:
            list[position] = list[position-1]
            position = position - 1

        list[position] = curr
    return list
