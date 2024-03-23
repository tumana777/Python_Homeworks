"""
დაწერეთ ფუნქცია, რომელსაც ატრიბუტად გადაეცემა რიცხვებისგან შემდგარი Queue, ფუნქციამ უნდა დაბეჭდოს 
ნაკადის სახელი, რიგიდან ამოღებული მნიშვნელობა და არის თუ არა ეს რიცხვი ლუწი. გაუშვით სამი ნაკადი(thread) 
და მხოლოდ ამის შემდეგ შეავსეთ რიგი(queue). საბოლოოდ დააჯოინეთ და დაბეჭდეთ რომ ყველა ამოცანა შესრულებულია.
"""

# import modules
import threading
from queue import Queue

# Create function for queue threading
def worker(task_queue):
    while True:
        task = task_queue.get()

        # Break loop
        if task is None:
            break
        
        # Thread name
        thread_name = threading.current_thread().name
        
        print(f"From {thread_name} --> {task} {"is even"if task % 2 == 0 else "is odd"}.")
        
        task_queue.task_done()
        
# Create queue instance
task_queue = Queue()
# Number of threads
num_workers = 3

# Threads list
threads = []

# Create and start threads in for loop
for i in range(num_workers):
    thread = threading.Thread(target=worker, args=(task_queue,), name=f"Thread {i+1}")
    thread.start()
    threads.append(thread)

# Tasks for threads
tasks = [5, 7, 12, 6, 8, 25, 9, 32, 13, 59]

# This for loop adds elemets(tasks) in queue
for task in tasks:
    task_queue.put(task)

# This for loop adds None instead of task
for _ in range(num_workers):
    task_queue.put(None)

# Join threads to main thread
for thread in threads:
    thread.join()

print("All tasks completed")




