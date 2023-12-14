from util.DBConnection import DBConnection
def getJob():
    try:
        item = '''select * from Company'''
        data = self.execute_return(item)
        return data

    except Exception as e:
        print(f"Error: {e}")