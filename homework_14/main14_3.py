# გამოიყენეთ organizations-100.csv
# წაიკითხეთ მოცემული csv ფაილი, შექმენით ახალი csv ფაილი “ssl_companies.csv” და ჩაწერეთ მხოლოდ აიდი, კომპანიის სახელი, 
# ვებ საიტი, ინდუსტრია და დასაქმებულების რაოდენობა ისეთი კომპანიების რომელთაც აქვთ ssl-ით დაცული ვებსაიტი(HTTPS)

import csv

with open('organizations-100.csv') as organizations:
    read = csv.DictReader(organizations)
    
    secured_companies = [row for row in read if row['Website'].startswith('https')]

keys_to_remove = ['Index', 'Country', 'Description', 'Founded']
    
for company in secured_companies:
    for key in keys_to_remove:
        company.pop(key)
    
    
headers = ['Organization Id','Name','Website','Industry','Number of employees']
    
with open('ssl_companies.csv', 'w', newline='') as ssl_companies:
    writer = csv.DictWriter(ssl_companies, fieldnames=headers)
    writer.writeheader()
    writer.writerows(secured_companies)