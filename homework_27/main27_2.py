"""
დაწერეთ ასინქრონული ფუნქცია, რომელიც რენდომად არჩეული დროით დააყოვნებს და დაბეჭდავს რიცხვებს 1-დან 10-მდე
"""
# Import modules
import random, asyncio

# Create async function
async def print_numbers():
    for i in range(1, 11):
        rand_time = random.randint(1, 5)
        await asyncio.sleep(rand_time)
        print(f"{i} -> delay time {rand_time} sec.")
        
# Run Async Function
asyncio.run(print_numbers())