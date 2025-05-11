from repository import Flower
from sqlalchemy.orm import Session

class FlowersRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_item(self, name: str, quantity: int, price_per_item: int):
        flower = Flower(name=name, quantity=quantity, price_per_item=price_per_item)
        self.db.add(flower)
        self.db.commit()
        self.db.refresh(flower)
        return flower

    def get_all(self):
        return self.db.query(Flower).all()

    def update_item(self, flower_id: int, quantity: int = None, price_per_item: int = None):
        flower = self.db.query(Flower).filter(Flower.id == flower_id).first()
        if not flower:
            return None
        if quantity is not None:
            flower.quantity = quantity
        if price_per_item is not None:
            flower.price_per_item = price_per_item
        self.db.commit()
        return flower

    def delete_item(self, flower_id: int):
        flower = self.db.query(Flower).filter(Flower.id == flower_id).first()
        if not flower:
            return None
        self.db.delete(flower)
        self.db.commit()
        return True






