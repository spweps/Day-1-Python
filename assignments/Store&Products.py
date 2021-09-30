class Store:

    def __init__(self, name):
        self.name = name
        self.product_list = []

    def add_product(self, new_product):
        self.product_list.append(new_product)

    def sell_product(self, id):
        self.product_list.pop(id)
    
    def inflation(self, percent_increase):
        for i in self.product_list:
            i.price = (i.price*percent_increase) + i.price   

    def set_clearance(self, category, percent_discount):
        self.category = category
        for i in self.product_list:
            i.price -= (i.price*percent_discount)
        return self


class Product:
    
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if not is_increased:
            self.price -= self.price*percent_change
            return self
        else:
            self.price += self.price*percent_change
            return self

# print(Product)
chlorox = Product ("Chlorox", 10, "cleaning")
# print(chlorox.name)
# print(chlorox.price)

# first_store = Store("Dojo's Dojo")
# first_store.add_product(chlorox)
# print(first_store.product_list[0].name)
# print(first_store.product_list[0].price)
# first_store.inflation(.0053)
# print(first_store.product_list[0].price)
print(chlorox.update_price(.1, True))
print(chlorox.price)