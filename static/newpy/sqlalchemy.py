#!/usr/bin/env python
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker, backref, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:', echo=True)
session = scoped_session(sessionmaker(bind=engine, autoflush=False))

Base = declarative_base()

class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String(128))
    author_id = Column(Integer, ForeignKey(Author.id), nullable=False)
    author = relationship(Author, backref=backref('books', lazy='dynamic'))

Base.metadata.create_all(engine)

author = Author(name="Frank Herbert")
book = Book(title="Dune", author=author)
session.add_all([author, book])
session.commit()
session.expunge_all()
