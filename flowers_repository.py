class UsersRepository:
    def __init__(self):
        self.flowers_db = {}
    def create_item(self, price_per_item: int, quantity: int, name: str):
        if name in self.flowers_db:
            current_price, current_quantity = self.flowers_db[name]
            self.flowers_db[name] = (current_price, current_quantity + 1)
        else:
            self.flowers_db[name] = (price_per_item, quantity)

    def get_all(self):
        return self.flowers_db



