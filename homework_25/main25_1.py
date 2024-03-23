"""
შექმენით რამდენიმე json ფაილი, დაწერეთ მოცემული json ფაილების პარსინგი რომელიც ფაილის სახელთან ერთად 
დაბეჭდავს json-ში არსებულ მონაცემებს და თითოეული ფაილისთვის გაუშვით ცალცალკე ნაკადი(thread
"""
# Import modules
import faker, json, threading

# Create fake class
fake = faker.Faker()

# Function to create json files
def create_json_file(file_name):
    
    # Create Data for json file
    json_data = {"data" : [{"id" : i, "name" : fake.name(),"country" : fake.country(),"email" : fake.email()} for i in range(1, 51)]}

    # Write data to json file
    with open(file_name, "w") as json_file:
        json.dump(json_data, json_file, indent=4)

# File names
files = ["fake_data1.json", "fake_data2.json", "fake_data3.json", "fake_data4.json"]

# Create json files
for file in files:
    create_json_file(file)

# Handle and Read Data from json files
def handling_data(file):
    with open(file) as json_file:
        data = json.load(json_file)
        
        for person in data["data"]:
            print(f"{file} -> {person["name"]} from {person["country"]}")

threads = []
# Start Threading
for file in files:
    thread = threading.Thread(target=handling_data, args=(file,))
    thread.start()
    threads.append(thread)

# Joining threads
for thread in threads:
    thread.join()

print("All threads completed!")