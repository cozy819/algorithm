input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    change_count = 0

    for index in range(0, len(string)-1):
        if string[index] != string[index + 1]:
            change_count += 1

    if change_count <= 2:
        flip_count = 1
    elif change_count > 2:
        flip_count = change_count - 1

    return flip_count


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
