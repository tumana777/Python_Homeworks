# შექმენით კლასი სახელწოდებით Student ატრიბუტებით, როგორიცაა name, student_id და courses(კურსების სია, რომელშიც 
# სტუდენტი არის ჩარიცხული). აღწერეთ სტუდენტის ინფორმაციის და კურსების ჩვენების მეთოდები. შექმენით რამდენიმე 
# ობიექტი და დაარეგისტრირეთ სხვადასხვა კურსებზე.

import inflect

p = inflect.engine()

def main():
    
    # Create Student Class
    class Student:
        # Initilize Attributes
        def __init__(self, name, student_id, courses):
            self.name = name
            self.student_id = student_id
            self.courses = courses
        # Display student's info method
        def student_info(self):
            print(f"Your ID is {self.student_id}, courses are {self.student_courses()}.")
        # Register Method
        def student_register(self):
            course = input(f'Dear {self.name}, please input course, where you want to register: ')
            print(f'You have successfully registered on "{course}" course.')
            self.courses.append(course)
            self.student_info()
        # Display student's courses method
        def student_courses(self):
            return p.join(self.courses)
                
    # Create Student Objects
    student1 = Student('Oto Tumanishvili', 1, ['Python', 'Javascript', 'Java'])
    student2 = Student('Levan Ananiashvili', 2, ['Python', 'C#', 'Ruby', 'HTML'])
    student3 = Student('Qetevan Maisuradze', 3, ['Python', 'C++', 'PHP'])
    
    # Call Student Methods
    student1.student_register()
    student2.student_register()
    student3.student_register()
    
main()