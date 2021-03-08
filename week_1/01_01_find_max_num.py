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
    for num in array:
        for compare_num in array:
            if num < compare_num:
                break
        else:
            return num


result2 = find_max_num2(input)
print(result2)
