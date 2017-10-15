from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


BaseModel = declarative_base()
engine = create_engine('sqlite:///restaurant.db')
BaseModel.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class RestaurantModel(BaseModel):
    __tablename__ = 'Restaurant'
    id = Column(Integer, Sequence('item_seq'), primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    location = Column(String(50), nullable=False, unique=False)

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_item(self):
        session.delete(self)
        session.commit()

    @classmethod
    def get_by_id(cls, rest_id):
        restaurant = session.query(RestaurantModel).filter_by(id=rest_id).first()
        if restaurant:
            return restaurant
        return None

    @classmethod
    def get_all(cls):
        all = session.query(RestaurantModel).all()
        return all
