student_grade={}
student_grade={"Kajari":98,"Subash":99,"Anahad":98,"Likhit":88,"Aman":90,"Preet":86,"Ruby":65}
def add_grades():
    #student_grade={}
    #student_grade={"Kajari":98,"Subash":99,"Anahad":98,"Likhit":88,"Aman":90,"Preet":86,"Ruby":65}
    n1=input("Please enter the name: ")
    g1=input("Please enter the grade: ")
    student_grade[n1]=str (g1)
    print("\n Updated list\n")
    print(student_grade)

def search_grades():
    search_name1=input("Enter the name you want to search: ")
    if search_name1 in student_grade.keys():
        print("Name: "+search_name+"\nGrade: "+student_grade[search_name])
    else:
        print("not found")



def update_grades():
    print(student_grade)
    search_name2=input("Enter the name you want to update grades: ")
    new_grade= input("Enter new grade between 1-100: ")
    if search_name2 in student_grade.keys():
        student_grade[search_name2]= new_grade
        print("\n Updated list\n")
        print(student_grade)
    else:
        print("Name not found")

def delete_grades():
    print(student_grade)
    search_name3=input("Enter the name whose grade you want to delete")
    if search_name3 in student_grade.keys():
        student_grade.pop(search_name3)
        print("\n Updated list\n")
        print(student_grade)
    else:
         print("Name not found")


def options():
    option1=input("Please select from options 1, 2, 3 or 4 \n 1. Add a student's grade  "
                  +"\n 2. Search Studdent's grade \n 3. Delete a student's grade"+ "\n 4. Update student's grade\n You selected :")
    if option1=="1":
         add_grades()
    elif option1=="2":
        search_grades()
    elif option1=="3":
        delete_grades()
    elif option1=="4":
        update_grades()
    else:
        print("\n Please select from options 1-4 !\n\n")
        options()

options()
# search_grades()       
# update_grades()
# delete_grades()
    



