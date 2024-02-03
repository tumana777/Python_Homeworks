# დაწერეთ პითონის პროგრამა, რომელიც შექმნის ტექსტურ ფაილს და მასში ჩაწერს 1000 ხაზს(ტექსტს არ აქვს მნიშვნელობა) 
# თავისი ნუმერაციით, შემდეგ წაიკითხეთ ეს ფაილი და დაბეჭდეთ ხაზების რაოდენობა, თუ რამდენია შევსებული.

with open('test1.txt', 'w') as file:
    for i in range(1, 1001):
        file.write(f'line {i}: I love Python\n')
        
with open('test1.txt') as read_file:
    print(read_file.read())
    
    # Method 1 for counting lines
    read_file.seek(0)
    lines = read_file.readlines()
    print(f'There is {len(lines)} lines in test file')
    
    
# Method 2 for counting lines
with open('test1.txt') as read_file_lines:
    lines = read_file_lines.readlines()
    print(f'There is {len(lines)} lines in test file')
