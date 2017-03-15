from flask import Flask, render_template
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    return render_template('menu.html', restaurant = restaurant, items = items)

#Task1 : create new items
@app.route('/restaurant/<int:restaurant_id>/create/')
def createMenuItem(restaurant_id):
    return 'Page to create new menu item for %s ' % restaurant_id

#Task2 : edit menu items
@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return 'Page to edit menu items for %s ' % restaurant_id

#Task3 : delete menu items
@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return 'Page to delete menu items from %s menu' % restaurant_id

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
