from sqlalchemy import Column, Float, Integer, Text
from sqlalchemy.orm import Mapped, declarative_base, mapped_column
from sqlalchemy.orm.base import Mapped

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    name = mapped_column(Text, nullable=False)
    id = mapped_column(Integer, primary_key=True)
    size = mapped_column(Float)
