from database import Base, engine
from models import Item


def create_database():
    print("Creating database ...")
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_database()