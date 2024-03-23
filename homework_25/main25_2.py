"""
დაწერეთ ფუნქცია, რომელსაც ატრიბუტად გადაეცემა რიცხვებისგან შემდგარი Queue, ფუნქციამ უნდა დაბეჭდოს 
ნაკადის სახელი, რიგიდან ამოღებული მნიშვნელობა და არის თუ არა ეს რიცხვი ლუწი. გაუშვით სამი ნაკადი(thread) 
და მხოლოდ ამის შემდეგ შეავსეთ რიგი(queue). საბოლოოდ დააჯოინეთ და დაბეჭდეთ რომ ყველა ამოცანა შესრულებულია.
"""

import threading
from queue import Queue

def worker(task_queue):
    while True:
        task = task_queue.get()
        
        if task is None:
            break
        
        print(f"From {thread.name} --> {task} {"is even"if task % 2 == 0 else "is odd"}.")
        
        task_queue.task_done()
        
task_queue = Queue()

tasks = [5, 7, 12, 6, 8, 25, 9]

for task in tasks:
    task_queue.put(task)

num_workers = 3

threads = []
for i in range(num_workers):
    thread = threading.Thread(target=worker, args=(task_queue,), name=f"Thread {i+1}")
    thread.start()
    threads.append(thread)

for _ in range(num_workers):
    task_queue.put(None)
    
for thread in threads:
    thread.join()

print("All tasks completed")




