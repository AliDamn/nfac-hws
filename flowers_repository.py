class UsersRepository:
    def __init__(self):
        self.flowers_db = {}

    def create_item(self, price_per_item: int, quantity: int, name: str):
        if name in self.flowers_db:
            current_price, current_quantity = self.flowers_db[name]
            self.flowers_db[name] = (current_price, current_quantity + quantity)
        else:
            self.flowers_db[name] = (price_per_item, quantity)

    def get_all(self):
      return [
        {"name": name, "price_per_item": data[0], "quantity": data[1]}
        for name, data in self.flowers_db.items()
    ]





