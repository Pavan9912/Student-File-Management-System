def AddStudent():
    sid=input("Enter the students id: ")
    student_name=input("Enter the students name: ")
    Course = input("Enter the course: ")
    with open("students.txt","a") as f:
        f.write(f"{sid},{student_name},{Course} \n")
    print("Student added successfully")
def ViewStudents():
        try:
            with open("students.txt","r") as file:
                data=file.read()
            if not data:
                print("No student details are found")
            else:
                print(data)
        except FileNotFoundError:
             print("No students record are found")
def SearchStudent():
    searchId = input("Enter Student ID: ")

    try:
        with open("students.txt", "r") as fil:
            flag = False

            for line in fil:
                stdID, stdName, stdCourse = line.strip().split(",")

                if searchId == stdID:
                    print(f"Student ID: {stdID}")
                    print(f"Student Name: {stdName}")
                    print(f"Course: {stdCourse}")
                    flag = True
                    break
            if not flag:
                print("Student not found")
    except FileNotFoundError:
        print("Student not found")
def CountTotalStudents():
    try:
        with open("students.txt","r") as file1:
            data1 = len(file1.readlines())
            print(f"Total Students: {data1}")
    except FileNotFoundError:
        print(f"no records found")
def DeleteStudent():
    deleteID=input("Enter the student id : ")
    try:
        with open("students.txt", "r") as fi:
            records = fi.readlines()
        flag = False
        with open("students.txt", "w") as file:
            for line in records:
                stdID, stdName, stdCourse = line.strip().split(",")
                if deleteID != stdID:
                    file.write(line)
                else:
                    flag=True
        if flag:
            print("Student deleted successfully")
        else:
            print("student id not found")
    except FileNotFoundError:
        print("no Student record found")
while True:
     
    print("\n=== Student File Management System ====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Count Total Students")
    print("5. Delete Student")
    print("6. Exit")
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            AddStudent()
        case "2":
            ViewStudents()
        case "3":
            SearchStudent()
        case "4":
            CountTotalStudents()
        case "5":
            DeleteStudent()
        case "6":
            print("Thank you for using Student File Management System")
            break
        case _:
            print("Invalid Choice!")
