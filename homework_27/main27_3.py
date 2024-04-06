"""
დაწერეთ ასინქრონული ფუნქცია,რომელიც დააბრუნებს ატრიბუტად გადაწოდებული რიცხვის კვადრატს, 
იმ შემთხვევაში თუ ეს რიცხვი არის ლუწი, ამის შესამოწმებლად დაწერეთ მეორე ასინქრონული ფუნქცია. 
შესამოწმებლად შექმენით რამდენიმე თასქი, გამოიყენეთ gather მეთოდი.
"""

import asyncio, random

num_list = list(range(1, 11))

async def square_number(num, delay):
    print(f"Function to square {num}, Started:")
    await asyncio.sleep(delay)
    print(f"{num} squared is {num ** 2}, working time -> {delay} secs.")

async def check_if_even(numbers):
    tasks = [square_number(number, random.randint(1, 5)) for number in numbers if number % 2 == 0]
    
    all_tasks = asyncio.gather(*tasks)
    await all_tasks

asyncio.run(check_if_even(num_list))