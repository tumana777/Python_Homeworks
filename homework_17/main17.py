# აღწერეთ ორი კლასი შემდეგი მონაცემების მიხედვით:

# Person:
# name
# deposit (default value = 1000, მიუთითებს ამჟამად რამდენი აქვს დეპოზიტზე)
# loan (default value = 0, მიუთითებს ამჟამად რამდენი აქვს სესხი აღებული)

# House:
# ID – ბინის საკატასტრო კოდი
# price – ბინის ფასი
# owner – სახლის მეპატრონე (Person ტიპის ობიექტი)
# status – ახალი ბინის დამატებისას სტატუსი არის ყოველთვის “გასაყიდი”

# გაითვალისწინეთ owner-ის მნიშვნელობა არის Person კლასის ობიექტი
# Person კლასში დაამატეთ __str__ მეთოდი რომელიც დააბრუნებს პიროვნების სრულ ინფორმაციას

# შექმენით ორი Person კლასის ობიექტი(მაგალითად ერთი მეპატრონე, მეორე მყიდველი). ასევე შექმენით House კლასის ობიექტი რომლის 
# owner იქნება ერთ-ერთი Person ობიექტი

# House კლასში დაამატეთ ბინის გაყიდვის მეთოდი, რომლის დროსაც პარამეტრებად გადაეცემა მყიდველი, თუ მეტი პარამეტრი არ გადაეცემა,
# ამ დროს უნდა შესრულდეს ბინის გაყიდვის ოპერაცია(გამყიდველის deposit უნდა გაიზარდოს ბინის ღირებულებით, უნდა შეიცვალოს 
# owner და status უნდა გახდეს “გაყიდული”, დაბეჭდეთ შესაბამისი ტექსტი). თუ ამ მეთოდის გამოძახების დროს მყიდველის გარდა 
# პარამეტრად გადაეცა კიდევ ერთი რიცხვი, მაშინ შესრულდეს ბინის სესხით გაყიდვის ოპერაცია, სადაც პარამეტრად გადაცემული რიცხვი 
# მიუთითებს მყიდველის მიერ აღებული სესხის რაოდენობას, მეთოდმა კი უნდა შეასრულოს შემდეგი ოპერაციები: გამყიდველის deposit 
# უნდა გაიზარდოს ბინის ღირებულებით, owner უნდა შეიცვალოს, status გახდეს “გაყიდული სესხით”, მყიდველის სესხი (loan) 
# უნდა გაიზარდოს შესაბამისი რაოდენობით და დაიბეჭდოს გაყიდვის შესაბამისი შეტყობინება.

# კლასის გარეთ მოახდინეთ აღწერილი ფუნქციების გამოძახება

# Create Person Class
class Person:
    # Initilize Parameters
    def __init__(self, name, deposit = 1000, loan = 0):
        self.name = name
        self.deposit = deposit
        self.loan = loan
        
    # Display Person's Info
    def __str__(self):
        return f"Person's name is {self.name}, deposit is ${self.deposit:,.0f} and loan is ${self.loan}."

# Create House Class
class House:
    # Initilize Parameters
    def __init__(self, house_ID, price, owner, status = 'for sale'):
        self.house_ID = house_ID
        self.price = price
        self.owner = owner
        self.status = status
        
    # House Selling Method
    def selling(self, buyer, opt_arg = 0):
        if opt_arg:
            if opt_arg + buyer.deposit >= self.price:
                self.owner.deposit += self.price
                self.owner = buyer
                self.status = 'sold out by loan'
                buyer.loan += opt_arg
                buyer.deposit -= self.price - opt_arg
            else:
                print(f'Dear {buyer.name}, try to loan ${self.price - (opt_arg + buyer.deposit):,.0f} more!')
        else:
            if buyer.deposit >= self.price:
                buyer.deposit -= self.price
                self.owner.deposit += self.price
                self.owner = buyer
                self.status = 'sold out'
            else:
                print(f'Dear {buyer.name}, you have not enough deposit to buy the house, try to buy by loan!')
        print(f'The house is {self.status} and house owner is {self.owner.name}.')

# Create Person Objects
person_seller = Person('Oto', 20000)
person_buyer = Person('Niko', 50000)

# Create and sell house
house = House('01.72', 100000, person_seller)
house.selling(person_buyer, 60000)
print(person_seller)
print(person_buyer)

# Create Person Objects
person_seller1 = Person('Levan', 40000)
person_buyer1 = Person('Giorgi', 90000)

# Create and sell house
house1 = House('01.72', 200000, person_seller1)
house1.selling(person_buyer1, 100000)
print(person_seller1)
print(person_buyer1)