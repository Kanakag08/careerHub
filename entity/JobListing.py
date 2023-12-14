class JobListing(DBConnection):
    def create(self):
        item = '''create table if not exists JobListing (JobID INT PRIMARY KEY,
                                                        companyID INT,
                                                        JobTitle VARCHAR(60),
                                                        JobDescription varchar(70),
                                                        JobLocation VARCHAR(50),
                                                        Salary int,
                                                        JobType VARCHAR(50),
                                                        PostedDate DATE,
                                                        FOREIGN KEY (companyID) REFERENCES Company(companyID) )'''
        self.execute(item)