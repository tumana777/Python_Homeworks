# დაწერეთ პითონის პროგრამა რომელიც ტერმინალში გვიჩვენებს მიმდინარე დროს ერთ ხაზზე სანამ ჩვენ არ გავაჩერებთ (Ctrl+c)

import time
import os

while True:
    time_now = time.strftime("%H:%M:%S")
    
    os.system('cls||clear') # აქ დაგუგლული მოვედი :) ასუფთავებს ტერმინალს
    
    print(f"Current time - {time_now}")
    
    time.sleep(1) # აქაც დაგუგლული მოვედი :) ეს კოდი ასრულებს ციკლს ყოველ 1 წამში
    
