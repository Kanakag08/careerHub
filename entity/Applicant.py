#applicant class
class Applicant(DBConnection):
    def create(self):
        item = '''create table if not exists Applicant (ApplicantID INT PRIMARY KEY,
                                                        FirstName VARCHAR(50),
                                                        LastName VARCHAR(50),
                                                        Email VARCHAR(50),
                                                        Phone VARCHAR(20),
                                                        Resume TEXT)'''
        self.execute(item)