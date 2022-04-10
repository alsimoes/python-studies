import db
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=db.engine)
session = Session()

for s in session.query(db.transactions).all():
    print(s.transaction_id, s.price)

print("*"*20)
print("Transactions with price over 40:")

for s in session.query(db.transactions).filter(db.transactions.price>40):
    print(s.transaction_id, s.price)