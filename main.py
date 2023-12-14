from dao.createTable import createTable
from dao.getJob import getJob
from dao.insertJob import insertJob
from dao.applyJob import applyJob
from dao.getApplicant import getApplicant
from dao.createProfile import createProfile
if __name__=="__main__":
    try:
        createTable()
        while True:
            print("Enter 1 to get Job:")
            print("Enter 2 to insert Job: ")
            print("Enter 3 to apply for job: ")
            print("Enter 4 to get Applicants: ")
            print("Enter 5 to create profile: ")
            print("Enter 6 to Exit: ")

            a=input("Enter your choice: ")
            if a == '1':
                getJob()
            elif a == '2':
                insertJob()
            elif a == '3':
                applyJob()
            elif a == '4':
                getApplicant()
            elif a == '5':
                createProfile()
            elif a =='6':
                break
            else:
                print("Invalid Choice: ")

    except Exception as e:
        print(f"Error: {e}")

