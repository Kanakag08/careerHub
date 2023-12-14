from util.DBConnection import DBConnection
def getApplicant(self):
    try:
        item = 'select * from JobListing'
        data = self.execute_return(item)
        return data

    except Exception as e:
        print(f"Error: {e}")


