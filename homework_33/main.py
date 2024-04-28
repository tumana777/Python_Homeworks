import psycopg2

HOST = "localhost"
PORT = 5432
DATABASE = "departments"
USER = "postgres"
PASSWORD = ""

conn = psycopg2.connect(host=HOST, port=PORT, database=DATABASE, user=USER, password=PASSWORD)
cursor = conn.cursor()

create_table_query = "create table department(departmentID serial primary key not null, departmentname varchar(30))"
create_table_query1 = "create table employee(employeeID serial primary key not null, fullname varchar(40), hiredate date default now(), departmentID int)"

cursor.execute(create_table_query)
cursor.execute(create_table_query1)
conn.commit()

constraint_query = "alter table employee add constraint department_cont foreign key(departmentID) references department(departmentID)"

cursor.execute(constraint_query)
conn.commit()

insert_query = "insert into department(departmentname) values('IT'), ('Finances'), ('HR'), ('Marketing'), ('Sales')"
insert_query1 = "insert into employee(fullname, departmentID) values('Oto Tumanishvili', 1), ('Levan Maisuradze', 3), ('Akaki Nioradze', 2), ('Mariam Ananiashvili', 3), ('Davit Lobjanidze', 4), ('Tinatin Chkheidze', 1), ('Ketevan Tushishvili', 5), ('Saba Salia', 3)"

cursor.execute(insert_query)
cursor.execute(insert_query1)
conn.commit()

select_query = "select fullname, departmentname, hiredate from employee inner join department on employee.departmentID = department.departmentID"

cursor.execute(select_query)
result = cursor.fetchall()

for employee in result:
    print(employee)

cursor.close()
conn.close()