import csv
from src.publicity_campaign import most_requested_dish


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: {path_to_file}")

    try:
        with open(path_to_file, mode="r", encoding="utf-8") as file:
            order_history = csv.reader(file, delimiter=",", quotechar='\n')

            result = [
                most_requested_dish(order_history, "maria"),
            ]

        with open("data/mkt_campaign.txt", mode="w", encoding="utf-8") as file:
            for line in result:
                file.write(f"{line}")

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")
