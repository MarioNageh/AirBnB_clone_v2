import os
import urllib
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, DateTime, PrimaryKeyConstraint, SmallInteger, ForeignKey, \
    Numeric
from sqlalchemy.orm import declarative_base, sessionmaker, relationship  # Use the updated import statement

password = urllib.parse.quote("Mario123!@#")
engine = create_engine(f'mysql+mysqldb://root:{password}@127.0.0.1:3307/hbnb_dev_db', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    __table_args__ = (
        PrimaryKeyConstraint('id', name='user_pk'),
        # Index('title_content_index' 'title', 'content'),  # composite index on title and content

    )


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    orders = relationship("Order", backref='customer')


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False)
    cost_price = Column(Numeric(10, 2), nullable=False)
    selling_price = Column(Numeric(10, 2), nullable=False)


#     orders = relationship("Order", backref='customer')


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True)
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    date_placed = Column(DateTime(), default=datetime.now)
    line_items = relationship("OrderLine",primaryjoin="Order.id == OrderLine.order_id", backref='order')


class OrderLine(Base):
    __tablename__ = 'order_lines'
    id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey('orders.id'))
    item_id = Column(Integer(), ForeignKey('items.id'))
    quantity = Column(SmallInteger())
    item = relationship("Item")


Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

customer_1 = Customer(first_name='John', last_name='Lara', username='johnlara',
                      email='aaa@aa.com')

customer_2 = Customer(first_name='Mary', last_name='Lara', username='marylara',
                      email="asd@ADA.com")

customer_3 = Customer(first_name='Henry', last_name='Lara', username='henrylara',
                        email='aa@aaaa.com')

item_1 = Item(name='Chair', cost_price=9.21, selling_price=10.81)
item_2 = Item(name='Pen', cost_price=3.45, selling_price=4.51)
item_3 = Item(name='Headphone', cost_price=15.52, selling_price=16.81)

order_1 = Order(customer_id=1)
orderline_1 = OrderLine(order_id=1, item_id=1, quantity=3)
orderline_2 = OrderLine(order_id=1, item_id=2, quantity=2)
orderline_3 = OrderLine(order_id=1, item_id=3, quantity=1)

session.add_all([customer_1, customer_2, customer_3, item_1, item_2, item_3, order_1, orderline_1, orderline_2, orderline_3])

session.commit()


# query
# customer = session.query(Customer).filter_by(first_name='John').first()
# print(customer.first_name, customer.last_name)
# customer_orders = customer.orders
# print(customer_orders)

# order = session.query(Order).filter_by(id=1).first()
# print(order.customer.first_name, order.customer.last_name)
# print(order.line_items)

order_line = session.query(OrderLine).filter_by(id=1).first()
print(order_line.order.customer.first_name, order_line.order.customer.last_name)