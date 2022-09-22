from collections import Counter


def most_requested_dish(dishes, client):
    requested_dish = list()

    for name, dish, _ in dishes:
        if name == client:
            requested_dish.append(dish)
        most_requested = Counter(requested_dish)
    return max(most_requested)
