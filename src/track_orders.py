class TrackOrders:
    def __init__(self):
        self._orders = list()

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self._orders)

    def add_new_order(self, customer, order, day):
        return self._orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        ordered_dish_per_customer = dict()

        for client, dish, _ in self._orders:
            if client == customer:
                ordered_dish_per_customer[dish] = dish
        return max(ordered_dish_per_customer)

    def get_never_ordered_per_customer(self, customer):
        never_ordered_per_customer = set()
        customers = set()

        for client, dish, _ in self._orders:
            never_ordered_per_customer.add(dish)
            if client == customer:
                customers.add(dish)
        return never_ordered_per_customer.difference(customers)

    def get_days_never_visited_per_customer(self, customer):
        never_days_visited_per_customer = set()
        customers = set()

        for client, _, day in self._orders:
            never_days_visited_per_customer.add(day)
            if client == customer:
                customers.add(day)
        return never_days_visited_per_customer.difference(customers)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
