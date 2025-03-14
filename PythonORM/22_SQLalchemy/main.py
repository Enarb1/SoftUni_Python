from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)

with Session() as session:
    user = User(
        first_name="John",
        last_name="Smith",
        age=36
    )

    session.add(user)
    session.commit()