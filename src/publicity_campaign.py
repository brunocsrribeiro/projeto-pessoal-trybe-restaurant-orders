from collections import Counter


def most_requested_dish(orders, client):
    requested_dish = list()

    for name, dish, _ in orders:
        if name == client:
            requested_dish.append(dish)
        most_requested = Counter(requested_dish)
    return most_requested.most_common()[0][0]


def get_burger_orders(orders, client, food):
    requested_burgers = list()

    for name, dish, _ in orders:
        if name == client and dish == food:
            requested_burgers.append(dish)
    number_of_burgers = len(requested_burgers)
    print(number_of_burgers)
    return number_of_burgers


def dish_not_ordered(orders, client):
    get_dishes = set()
    get_clients = set()

    for name, dish, _ in orders:
        get_dishes.add(dish)
        if name == client:
            get_clients.add(dish)
    return get_dishes.difference(get_clients)


def get_days_never_visited(orders, client):
    get_days = set()
    get_clients = set()

    for name, _, day in orders:
        get_days.add(day)
        if name == client:
            get_clients.add(day)
    return get_days.difference(get_clients)
