from util.DBConnection import DBConnection

def createProfile(self):
    try:
        FirstName = input("Enter first Name: ")
        LastName = input("Enter last Name: ")
        Email = input("Enter email: ")
        Phone = input("Enter Phone: ")
        item = f'''insert into Applicant values('{FirstName}','{LastName}','{Email}','{Phone}')'''
        self.execute(item)

    except Exception as e:
        print(f"Error: {e}")