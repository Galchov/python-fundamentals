class Storage:
    __storage = 0

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product):
        if not Storage.__storage == self.capacity:
            self.storage.append(product)
            Storage.__storage += 1

    def get_products(self):
        return self.storage