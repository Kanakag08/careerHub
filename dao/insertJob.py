from util.DBConnection import DBConnection
def insertJob(self):
    try:
        companyID = int(input("Enter the company ID: "))
        companyName = input("Enter the company name: ")
        location = input("Enter the Location: ")
        item = f'''Insert into Company Values({companyID},'{companyName}','{location}')'''
        self.execute(item)
    except Exception as e:
        print(f"Error: {e}")