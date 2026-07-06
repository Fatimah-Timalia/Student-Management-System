#add student,view student, search student, delete student, exit
class Student:
    def __init__(self,id,name,age,marks):
        self.id = id
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(f"Id: {self.id}\nName: {self.name}\nAge: {self.age}\nMarks: {self.marks}")


students = []


while True:
    print("1. Add Student \n2. View Student \n3. Search Student \n4. Delete Student \n5.Update Student \n6. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        found = False
        id = int(input("Enter Student Id: "))
        for i in students:
            if i.id == id:
                print("student id already exists")
                found = True
                break
        if found == True:
            continue
        name = input("Enter Student name: ")
        age = int(input("Enter Student age: "))
        marks = int(input("Enter Student marks: "))
        new_Student = Student(id,name,age,marks)
        students.append(new_Student)
    
    elif choice == 2:
        if len(students) == 0:
                print("Databse is empty!")
                continue
        for i in students:
            print()
            i.display()
    
    elif choice == 3:
        found = False
        search = int(input("Enter the ID of student you're searching for: "))
        for i in students:
            if i.id == search:
                print("Student found")
                i.display()
                found = True
                break
        if found == False:
            print("Student does not exists!")
    
    elif choice == 4:
        found = False
        delete = int(input("Enter ID of student you wanna delete from database:")) 
        for i in students:
            if i.id == delete:
                print(f"Student {delete} Deleted")
                students.remove(i)
                found = True
                break
        if found == False:
            print("Student does not exists")
    
    elif choice == 5:
        found = False
        update = int(input("enter id of Student u wanna update: "))
        for i in students:
            if i.id == update:
                found = True
                up = input("what do u wanna update? Choose one option: id,name,age,marks: ")
                if up.lower().strip() =="id":
                    exists = False
                    ch = int(input("Enter new ID: "))
                    for i in students:
                        if i.id == ch:
                            print("id already exists!")
                            exists = True
                            break
                    if exists == False:
                        i.id = ch
                        break
                elif up.lower().strip() =="name":
                    ch = input("Enter new name: ")
                    i.name = ch
                    break
                elif up.lower().strip() =="age":
                    ch = int(input("Enter new age: "))
                    i.age = ch
                    break
                elif up.lower().strip() =="marks":
                    ch = int(input("Enter new marks: "))
                    i.marks = ch
                    break
                else:
                    print("not a valid option")
                    break
        if found == False:
            print("Student does not exists")
            continue
                
    elif choice == 6:
        break

    else:
        print("Invalid Choice!")
