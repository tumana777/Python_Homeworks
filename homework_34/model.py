from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Double
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import func

HOST = "localhost"
PORT = 5432
DATABASE = "products"
USER = "postgres"
PASSWORD = ""

engine = create_engine(f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

Base = declarative_base()

class Category(Base):

    __tablename__ = "categories"

    category_id = Column("category_id", Integer, primary_key=True, autoincrement=True)
    category_name = Column("category_name", String(20))
    
    def __init__(self, category_name):
        self.category_name = category_name

class Product(Base):

    __tablename__ = "products"

    product_id = Column("product_id", Integer, primary_key=True, autoincrement=True)
    product_name = Column("product_name", String(20))
    product_price = Column("product_price", Double)
    stock_quantity = Column("stock_quantity", Integer)
    category_id = Column("category_id", Integer, ForeignKey("categories.category_id"))
    
    def __init__(self, category_id, product_name, product_price, stock_quantity):
        self.category_id = category_id
        self.product_name = product_name
        self.product_price = product_price
        self.stock_quantity = stock_quantity

class Order(Base):

    __tablename__ = "orders"

    order_id = Column("order_id", Integer, primary_key=True, autoincrement=True)
    product_id = Column("product_id", Integer, ForeignKey("products.product_id"))
    quantity = Column("quantity", Integer)
    order_date = Column("order_date", DateTime, server_default=func.date_trunc('second', func.now()))
    status = Column("status", String(20))
    
    def __init__(self, product_id, quantity, status="Pending"):
        self.product_id = product_id
        self.quantity = quantity
        self.status = status

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()