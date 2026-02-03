from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    completed = Column(Boolean, default=False)
    pet_id = Column(Integer, ForeignKey('pets.id'))# foreign key to link to Pet.id

    # the other side of theone-to-many relationship.
    pet = relationship('Pet', back_populates='tasks')

    def __repr__(self):
        return f'<Task id={self.id} description="{self.description}" pet_id={self.pet_id}>'