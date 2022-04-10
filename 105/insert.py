import db
from sqlalchemy.orm import sessionmaker
import random

Session = sessionmaker(bind=db.engine)
session = Session()

for t in range(11,20):
    item_id = random.randint(0,1000)
    price = random.randint(20,50)

    tr = db.transactions(t, '2022/04/10', item_id, price)
    session.add(tr)

session.commit()