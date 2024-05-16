from sqlalchemy import create_engine


from sqlalchemy_project.constants import URL
from sqlalchemy_project.db_management import DB
from sqlalchemy_project.tables import Project, Customer, Delivery
from sqlalchemy_project.tables import Order


engine = create_engine(URL)
Project.metadata.create_all(engine)
Customer.metadata.create_all(engine)
Order.metadata.create_all(engine)
Delivery.metadata.create_all(engine)

db = DB()


products = [
    ('Stalas', 119.99),
    ('Kede', 39.99),
    ('Vaizduoklis', 69.99),
    ('Kompiuteris', 1000.00),
]

customers = [
    ("Petras Petrauskas", "Petriukas@yahoo.com"),
    ("Jonas Jonauskas", "John@SAP.com"),
    ("Antanas RUndelis", "zuikis123@lnk.lt"),
]

orders = [
    (1, 1, 2000),
    (2, 2, 140),
    (3, 3, 2400)
]

deliveries = [
    ("LP Express", "nezinom dar" ),
    ("FedEX", "nezinom dar" ),
    ("FedEX", "nezinom dar" ),
]

# db.add_values_to_project_table(products)
# db.add_customers(customers)
# db.add_orders(orders)
db.add_order(1, 4, 2300)
db.add_customer("Karolis", "mano@el.p.lt")
