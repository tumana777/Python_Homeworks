# გამოიყენეთ titanic.csv
# წაიკითხეთ მოცემული csv ფაილი, შექმენით ახალი csv ფაილი “survived.csv” და ჩაწერეთ მხოლოდ გადარჩენილების ინფორმაცია.

import csv

with open('titanic.csv') as titanic:
    read = csv.DictReader(titanic)
    
    survived = [row for row in read if row['Survived'] == '1']

headers = ['PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']

with open('survived.csv', 'w', newline='') as all_survived:
    writer = csv.DictWriter(all_survived, fieldnames=headers)
    writer.writeheader()
    writer.writerows(survived)