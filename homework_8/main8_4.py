# დაწერეთ lambda ფუნქცია, რომელიც პასუხად დააბრუნებს სტრინგი არის თუ არა პალინდრომი, სტრინგები უნდა იყოს 
# შენახული ლისტში. დაწერეთ filter ფუნქციის გამოყენებით


lst = ["hello", "oto", "I", "world", "level", "car", "racecar", "others"]

palindromes = list(filter(lambda word: word == word[::-1], lst))

print(palindromes)