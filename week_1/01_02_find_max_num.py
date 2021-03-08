input = [3, 5, 6, 1, 2, 4]


def find_max_num_my(array):
    max = array[0]
    i = 0
    while i < len(array) - 1:
        if array[i] > array[i+1]:
            max = array[i]
        i = i + 1
    return max


result = find_max_num_my(input)
print(result)


def find_max_num2(array):
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num
    return max_num


result2 = find_max_num2(input)
print(result2)
