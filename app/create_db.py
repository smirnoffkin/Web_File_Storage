from database import sync_engine
import models


def create_database():
    print("Creating database ...")
    models.Base.metadata.create_all(bind=sync_engine)


if __name__ == "__main__":
    create_database()
