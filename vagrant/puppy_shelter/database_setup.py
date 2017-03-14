import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base  = declarative_base()

class Shelter(Base):
	__tablename__ = 'shelter'

	name = Column(String(100), nullable = False)
	address = Column(String(100), nullable = False)
	city = Column(String(100), nullable = False)
	state = Column(String(100), nullable = False)
	zipCode = Column(String(100), nullable = False)
	website = Column(String(100))
	id = Column(Integer, primary_key = True)

class Puppy(Base):
	__tablename__ = 'puppy'

	name = Column(String(20), nullable = False)
	id = Column(Integer, primary_key = True)
	dob = Column(String(10))
	gender = Column(String(7), nullable = False)
	weight = Column(String(10), nullable = False)
	shelter_id = Column(Integer, ForeignKey('shelter.id'))
	puppy = relationship(Shelter)
	picture = Column(String(100))

engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.create_all(engine)
