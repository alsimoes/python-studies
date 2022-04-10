import db
from sqlalchemy.orm import Session

session = Session(db.engine)

for s in session.query(db.transactions).all():
    print(s)

print("*"*100)
print("Transactions with price over 40:")

for s in session.query(db.transactions).filter(db.transactions.price>40):
    print(s)