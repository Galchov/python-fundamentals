class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        return [p for p in self.products if p[0] == first_letter]

    def __repr__(self):
        catalogue_info = f"Items in the {self.name} catalogue:\n"
        catalogue_info += '\n'.join(sorted(self.products))
        return catalogue_info