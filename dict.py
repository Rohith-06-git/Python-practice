student_database = {
    "Alice": {"Age": 14, "Math": 92, "Science": 88},
    "Bob": {"Age": 15, "Math": 75, "Science": 82},
    "Charlie": {"Age": 14, "Math": 64, "Science": 70}
}
print("Data of students named the below are available :\n")
for name in student_database :
    print(f"{name}")
print()
print("To get the full report of student Enter name below \n")

while True :
    try :
        student = input("Enter here or to quit enter 'q': ")
        if student.lower() == 'q':
           print("Thank you Have a Good Day !! ")
           break
        std_info = student_database[student]

        if std_info :
         total =  (student_database[student]["Math"] + student_database[student]["Science"] )
         percentage = (total / 200) * 100
         print(f"Age :{student_database[student]["Age"]}")
         print(f"Math score : {student_database[student]["Math"]}")
         print(f"Science score : {student_database[student]["Science"]}")
         print(f"Total score :{total}")
         print(f"Percentage : {percentage}")
        else :
           print("Student Data Not Found ")
    except ValueError :
       print("Invalid input")
        
