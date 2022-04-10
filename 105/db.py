from importlib.metadata import metadata
from sqlalchemy import create_engine, Column, String, Integer, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import registry
from dataclasses import dataclass, field
# from typing import Optional

engine = create_engine('sqlite:///105.sqllite', echo=True)
base = declarative_base()

mapper_registry = registry()

@mapper_registry.mapped
@dataclass
class transactions:
    
    __table__ = Table (
        'transactions',
        mapper_registry.metadata,
        Column("id", Integer, primary_key=True),
        Column("date", String),
        Column("item_id", Integer),
        Column("price", Integer)
    )

    id: int = field(init=False)
    date: str
    item_id: int
    price: int
    # price: Optional[int] = None


base.metadata.create_all(engine)