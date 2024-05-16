
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_project.constants import URL
from sqlalchemy_project.tables import Project
from sqlalchemy_project.tables import Customer, Order, Delivery


class DB:
    def __init__(self):
        self.engine = create_engine(URL)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def get_object_by_id(self, obj: object, id: int):
        return self.session.query(obj).get(id)

    def add_value_to_project_table(self, name, price):
        project = Project(name=name, price=price)
        self.session.add(project)
        self.session.commit()

    def add_values_to_project_table(self, data: list[tuple]):
        projects = [Project(name=d[0], price=d[1]) for d in data]
        self.session.add_all(projects)
        self.session.commit()

    def add_customer(self, name, contact):
        customer = Customer(name=name, contact=contact)
        self.session.add(customer)
        self.session.commit()

    def add_customers(self, customers_data: list[tuple]):
        customers = [Customer(name=data[0], contact=data[1]) for data in customers_data]
        self.session.add_all(customers)
        self.session.commit()

    def add_order(self, project_id, customer_id, total_amount):
        order = Order(project_id=project_id, customer_id=customer_id, total_amount=total_amount)
        self.session.add(order)
        self.session.commit()

    def add_orders(self, orders_data: list[tuple]):
        orders = [Order(project_id=data[0], customer_id=data[1], total_amount=data[2]) for data in orders_data]
        self.session.add_all(orders)
        self.session.commit()

    def add_delivery(self, project_id, customer_id, delivering_company, delivery_date):
        delivery = [Delivery(project_id=data[0], customer_id=data[1], delivering_company=data[2], delivery_date=data[3]) for data in delivery_data]
        self.session.add_all(delivery)
        self.session.commit()

    def add_deliveries(self, delivery_data: list[tuple]):
        deliveries = [Delivery(project_id=data[0], customer_id=data[1], total_amount=data[2]) for data in delivery_data]
        self.session.add_all(deliveries)
        self.session.commit()
