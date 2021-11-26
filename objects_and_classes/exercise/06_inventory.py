class Inventory:
    def __init__(self, __capacity):
        self.__capacity = __capacity
        self.items = []

    def add_item(self, item):
        if len(self.items) >= self.__capacity:
            return f"not enough room in the inventory"
        self.items.append(item)

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\n" \
               f"Capacity left: {self.__capacity - len(self.items)}"