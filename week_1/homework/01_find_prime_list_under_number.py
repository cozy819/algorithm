input = 20

def find_prime_list_under_number(number):
    result = []

    number_list = range(2, number + 1)

    for i in number_list:
        check = True
        divide_by_list = range(2, i + 1)
        for j in divide_by_list:
            if i % j == 0 and i != j:
                check = False

        if check:
            result.append(i)

    return result


result = find_prime_list_under_number(input)
print(result)