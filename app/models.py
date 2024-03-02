from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Author(Base):
    __tablename__ = 'author'
    author_id = Column(Integer, primary_key = True)
    name = Column(String)
    books = relationship("Book", back_populates = "author")

    def __repr__(self):
        return '<Author: {}>'.format(self.books)

class Book(Base):
    __tablename__ = 'book'
    book_id = Column(Integer, primary_key = True)
    author_id = Column(Integer, ForeignKey("author.author_id"))
    title = Column(String)