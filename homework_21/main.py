'''
შექმენით კლასი Product ატრიბუტებით name, price, quantity, შექმენით კლასის რამდენიმე ობიექტი, დაამატეთ ლისტში, 
დაწერეთ სერიალიზაციის მეთოდი, რომ კლასი გადაითარგმნოს JSON ფორმატში და ჩაწერეთ ფაილში, შემდეგ წაიკითხეთ 
ეს ფაილი, დაწერეთ დესერიალიზაციის მეთოდი, რომ ინფორმაცია გადაითარგმნოს Product კლასში და დაბეჭდეთ ყველა 
პროდუქტის ინფორმაცია
'''
# Importing json module
import json

# Create Product Class
class Product:
    # Initialize Parameters
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    # This method returns product info insted of object address
    def __str__(self) -> str:
        return f"Name: {self.name}, Price: {self.price:.2f}, Quantity: {self.quantity}"

# This function returns dictionary from Product class
def serialize_product(obj):
    # Checking if given object is Product class
    if isinstance(obj, Product):
        return {"Name" : obj.name, "Price" : obj.price, "Quantity" : obj.quantity}
    raise TypeError("Not a Product class!")
    
# Create some products
product1 = Product("Cola", 2.9, 10)
product2 = Product("Fanta", 2.5, 8)
product3 = Product("Lays", 2.95, 12)
product4 = Product("XL", 3.95, 15)
product5 = Product("Red-Bull", 5.1, 6)
product6 = Product("Snickers", 1.9, 14)

# Add products in list
product_list = [product1, product2, product3, product4, product5, product6]

# Writing products in file
with open("products.json", "w") as json_file:
    json.dump(product_list, json_file, default=serialize_product, indent=4)

# This function returns Product class object from given json object
def deserialize_json(json_obj):
    return Product(json_obj["Name"], json_obj["Price"], json_obj["Quantity"])

# Reading data from json file
with open("products.json") as file:
    deserialized_data = json.load(file, object_hook=deserialize_json)

# Printing deserialized product
for product in deserialized_data:
    print(product)


