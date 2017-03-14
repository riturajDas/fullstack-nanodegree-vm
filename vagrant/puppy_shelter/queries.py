from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Shelter, Puppy
import datetime

engine = create_engine('sqlite:///puppyshelter.db')
DBSession = sessionmaker(bind = engine)
session = DBSession()

#helper methods
def passesLeapDay(today):
	thisYear = today.timetuple()[0]
	if isLeapYear(thisYear):
		sixMonthsAgo = today - datetime.timedelta(days = 183)
		leapDay = datetime.dat(thisYear, 2, 29)
		return leapDay >= sixMonthsAgo
	else :
		return False

def isLeapYear(thisYear):
	if thisYear % 4 != 0:
		return False
	elif thisYear % 100 != 0:
		return True
	elif thisYear % 400 != 0:
		return False
	else :
		return True

def query_one():
	#order puppy names in ascending order
	result = session.query(Puppy.name).order_by(Puppy.name.asc()).all()
	for i in result:
		print i[0]
	print '\n'

def query_two():
	#order puppies acc. ascending age and are <6 months old
	today = datetime.date.today()
	if passesLeapDay(today):
		sixMonthsAgo = today - datetime.timedelta(days = 183)
	else :
		sixMonthsAgo = today - datetime.timedelta(days = 182)
	result = session.query(Puppy.name, Puppy.dob).filter(Puppy.dob >= sixMonthsAgo).order_by(Puppy.dob.asc())
	for i in result:
		print '{name}: {dob}'.format(name = i[0], dob = i[1])
	print '\n'

def query_three():
	#all puppies in ascending weight
	result = session.query(Puppy.name, Puppy.weight).order_by(Puppy.weight.asc()).all()
	for i in result:
		print i[0], i[1]
	print '\n'

def query_four():
	#all puppies grouped by their shelter
	result = session.query(Shelter, func.count(Puppy.id)).join(Puppy).group_by(Shelter.id).all()
	for i in result:
		print i[0].id, i[0].name, i[1]
	print '\n'

query_one()
query_two()
query_three()
query_four()
