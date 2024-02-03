# გამოიყენეთ organizations-100.csv
# წაიკითხეთ მოცემული csv ფაილი, შექმენით ახალი csv ფაილი “sorted_csv.csv” და ჩაწერეთ დასორტირებული 
# ინფორმაცია, დაასორტირეთ თანამშრომელთა რაოდენობის მიხედვით

import csv

with open('organizations-100.csv') as organizations:
    read = csv.DictReader(organizations)
    
    orgs = [row for row in read]
    
sorted_orgs = sorted(orgs, key=lambda x: int(x['Number of employees']))
    
headers = ['Index','Organization Id','Name','Website','Country','Description','Founded','Industry','Number of employees']

with open('sorted_csv.csv', 'w', newline='') as sorted_organizations:
    writer = csv.DictWriter(sorted_organizations, fieldnames=headers)
    writer.writeheader()
    writer.writerows(sorted_orgs)