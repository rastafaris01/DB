from sqlalchemy import create_engine
import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_project.constants import URL

engine = create_engine(URL)
Base = declarative_base()

class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    orders = relationship('Order', back_populates='project')

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.id} {self.name} - {self.price}: {self.created_date}"

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact = Column(String)
    registration_date = Column(DateTime, default=datetime.datetime.utcnow())
    orders = relationship('Order', back_populates='customer')

    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def __repr__(self):
        return f"<Customer(id={self.id}, name={self.name}, email={self.contact}, registration_date={self.registration_date})>"

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    order_date = Column(DateTime, default=datetime.datetime.utcnow)
    total_amount = Column(Float)

    project = relationship('Project', back_populates='orders')
    customer = relationship('Customer', back_populates='orders')

    def __init__(self, project_id, customer_id, total_amount):
        self.project_id = project_id
        self.customer_id = customer_id
        self.total_amount = total_amount

    def __repr__(self):
        return f"<Order(id={self.id}, project_id={self.project_id}, customer_id={self.customer_id}, order_date={self.order_date}, total_amount={self.total_amount})>"

class Delivery(Base):
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    delivering_company = Column(String)
    delivery_date = Column(DateTime, default=None)

    project = relationship('Project', back_populates='deliveries')
    customer = relationship('Customer', back_populates='deliveries')

    def __init__(self, project_id, customer_id, delivering_company, delivery_date):
        self.project_id = project_id
        self.customer_id = customer_id
        self.delivering_company = delivering_company
        self.delivery_date = delivery_date

    def __repr__(self):
        return f"Delivery(id={self.id}, project_id={self.project_id}, customer_id={self.customer_id}, delivering_company={self.delivering_company}, delivery_date={self.delivery_date}"


Base.metadata.create_all(bind=engine)
