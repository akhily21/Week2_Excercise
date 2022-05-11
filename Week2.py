def search(name):
    if student_details.get(name)==None:
        print("The student does not exist")
    else:
        print("The student grade is ",student_details[name])

student_details={
    "Ron": 10,
    "Jack": 9,
    "Jose": 5    
    }


while(1):  
#Student Grade search
    s=input("Do you want to search a student's grade?: Y or N")
    if(s=='Y'):
        name=input("Enter the name of the student")
        search(name)
    user_choice=input(" Do you wish to add a student? Enter A\n Do you want to delete a student? Enter D\n Do you want to update a student's grade? Enter U")

#Add or Delete records
    if(user_choice=='A'):
        name=input("Enter the name of the student you wish to add")
        grade=input("Enter the student's grade")
        student_details.update({name: grade})
        print("Student added successfully. Updated list is ", student_details)
    elif(user_choice=='D'):
        name=input("Enter the name of the student yu wish to delete")
        student_details.pop(name)
        print("Student deleted successfully. Updated list is ", student_details)
    elif(user_choice=='U'):
        name=input("Enter the name of the student you wish to update")
        grade=input("Enter the student's grade")
        student_details.update({name: grade})
        print("Student details updated successfully. Updated list is ", student_details)
    else:
        print('Invalid Choice')
    
        

   
    



    