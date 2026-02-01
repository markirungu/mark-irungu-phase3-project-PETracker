from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Pet(Base):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    species = Column(String)
    #NB, this is a part of the one to many relationship with task.

    # back_populates='pet' links to the `pet` attribute in the Task class.
    tasks = relationship('Task', back_populates='pet')

    def __repr__(self):
        return f'<Pet id={self.id} name="{self.name}" species="{self.species}">'