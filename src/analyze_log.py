import csv
from src.publicity_campaign import (
    most_requested_dish, get_burger_orders,
    dish_not_ordered, get_days)


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: {path_to_file}")

    try:
        with open(path_to_file, mode="r", encoding="utf-8") as file:
            order_history = list(
                csv.reader(file, delimiter=",", quotechar='\n'))

            result = [
                most_requested_dish(order_history, "maria"),
                get_burger_orders(order_history, "arnaldo", "hamburguer"),
                dish_not_ordered(order_history, "joao"),
                get_days(order_history, "joao")
            ]

        with open("data/mkt_campaign.txt", mode="w", encoding="utf-8") as file:
            for line in result:
                file.write(f"{line}\n")

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")
