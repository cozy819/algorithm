shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    switch = False

    menus.sort()
    n = len(orders)

    for i in range(n):
        current_min = 0
        current_max = len(menus) - 1
        current_guess = (current_min + current_max) // 2

        while current_min <= current_max:
            if menus[current_guess] == orders[i]:
                switch = True
                break
            elif menus[current_guess] < orders[i]:
                current_min = current_guess + 1
                switch = False
            else:
                current_max = current_guess - 1
                switch = False
            current_guess = (current_min + current_max) // 2

    return switch


def is_available_to_order_way2(menus, orders):
    menus_set = set(menus)
    for order in orders:
        if order not in menus_set:
            return False
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)