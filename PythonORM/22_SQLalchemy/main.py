import random

from sqlalchemy.orm import sessionmaker
from models import User, engine, City

Session = sessionmaker(bind=engine)

with Session() as session:
    users = session.query(User).all()
    for u in users:
        u.city_id = random.randint(1,5)
    session.commit()

