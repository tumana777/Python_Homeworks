"""
დაწერეთ ორი ასინქრონული ფუნქცია, ერთ-ერთი დააყოვნეთ 2 წამი, მეორე 5 წამი, 
დაბეჭდეთ მათი დაწყება და დასრულება, თასქები შექმენით ცალ-ცალკე და გაუშვით.
"""
# Import module
import asyncio,time

# Create acync functions
async def coding():
    print("Started Coding.")
    await asyncio.sleep(5)
    print("Ended Coding.")
    
async def play_billiards():
    print("Started Playing Billiards.")
    await asyncio.sleep(2)
    print("Ended Playing Billiards.")
    
async def main():
    # Create async tasks
    task1 = asyncio.create_task(coding())
    task2 = asyncio.create_task(play_billiards())
    await task1, task2 # Awaiting tasks

# Run main async function
asyncio.run(main())

