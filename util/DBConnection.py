import mysql.connector as sql
from datetime import datetime
# Database connectivity
class DbConnection:
    def open(self):
        try:
            self.conn = sql.connect(host='localhost',database='careerHub',user='root',password='Kagrawal@08')
            self.stmt = self.conn.cursor()
        except Exception as e:
            print("Database Not found: ")

    def close(self):
        try:
            self.conn.close()
        except Exception as e:
            print(str(e))

    def execute(self, item):
        self.open()
        try:
            self.stmt = self.conn.cursor()
            self.stmt.execute(item)
        except Exception as e:
            print(f"Error: {e}")
        else:
            self.conn.commit()
        finally:
            self.close()

    def execute_many(self, item, data):
        self.open()
        self.stmt = self.conn.cursor()
        try:
            self.stmt.executemany(item, data)
        except Exception as e:
            print('Invalid Data ')
        else:
            self.conn.commit()
        finally:
            self.close()

    def execute_return(self, item):
        self.open()
        self.stmt = self.conn.cursor()
        self.stmt.execute(item)
        data = self.stmt.fetchall()
        self.close()
        return data