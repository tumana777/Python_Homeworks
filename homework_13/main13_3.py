# დაწერეთ პითონის პროგრამა, რომელიც წაიკითხავს ორ ფაილს და მათ გაერთიანებულს ჩაწერს ახალ ტექსტურ ფაილში. 
# გაერთიანებული ფაილი წაიკითხეთ და დაბეჭდეთ ტერმინალში.

with open('test1.txt') as file1, open('test2.txt') as file2, open('test3.txt', 'w+') as file3:
    file1_data = file1.readlines()
    file2_data = file2.readlines()
    file3.writelines(file1_data + file2_data)
    file3.seek(0)
    print(file3.read())
