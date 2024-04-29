from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

HOST = "localhost"
PORT = 5432
DATABASE = "departments"
USER = "postgres"
PASSWORD = "I12fuckyou"

engine = create_engine(f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

Base = declarative_base()

class Department(Base):

    __tablename__ = "department"

    departmentid = Column("departmentid", Integer, primary_key=True, autoincrement=True)
    departmentname = Column("departmentname", String(30))

class Employee(Base):
    
    __tablename__ = "employee"

    employeeid = Column("employeeid", Integer, primary_key=True, autoincrement=True)
    fullname = Column("fullname", String(40))
    hiredate = Column("hiredate", Date)
    departmentid = Column("departmentid", Integer, ForeignKey("department.departmentid"))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()