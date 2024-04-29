from model import session, Department, Employee

joined_query = session.query(Employee.fullname, Employee.hiredate, Department.departmentname).join(Department).all()

for name, date, department in joined_query:
    print(name, department, date, sep=', ')