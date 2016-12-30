def sort(list):
    if len(list) <= 1:
        return list

    pivot = int(len(list) / 2)
    left = sort(list[:pivot])
    right = sort(list[pivot:])

    result = []
    li, ri = 0, 0
    while li < len(left) and ri < len(right):
        if left[li] <= right[ri]:
            result.append(left[li])
            li += 1
        else:
            result.append(right[ri])
            ri += 1

    result.extend(left[li:])
    result.extend(right[ri:])

    return result
