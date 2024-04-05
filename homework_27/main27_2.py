"""
დაწერეთ ასინქრონული ფუნქცია, რომელიც რენდომად არჩეული დროით დააყოვნებს და დაბეჭდავს რიცხვებს 1-დან 10-მდე
"""
import asyncio, random
from codetiming import Timer

async def print_numbers(number, delay):
    timer = Timer(text=f"Printed: {number} -> in {{:.2f}} seconds")
    timer.start()
    print(f"Started function to print {number}")
    await asyncio.sleep(delay)
    timer.stop()

async def main():
    tasks = []
    
    for i in range(1, 11):
        number = f"Number {i}"
        delay = random.randint(1, 5)
        tasks.append(print_numbers(number, delay))
    
    all_tasks = asyncio.gather(*tasks)
    await all_tasks

asyncio.run(main())