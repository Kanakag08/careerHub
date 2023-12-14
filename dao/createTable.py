from util.DBConnection import DBConnection

def createTable():
    conn=None
    try:
            conn,stmt=DBConnection.open()
            if conn:
                item = '''create table if not exists company(companyID int primary key,
                                                                   companyName varchar(50),
                                                                   location varchar(60))'''
                self.execute(item)

                item = '''create table if not exists Applicant (ApplicantID INT PRIMARY KEY,
                                                                        FirstName VARCHAR(50),
                                                                        LastName VARCHAR(50),
                                                                        Email VARCHAR(50),
                                                                        Phone VARCHAR(20),
                                                                        Resume TEXT)'''
                self.execute(item)

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

                item = '''Create table if not exists JobApplication(ApplicationID INT PRIMARY KEY,
                                                                          JobID INT,
                                                                          ApplicantID INT,
                                                                          ApplicationDate DATETIME,
                                                                          CoverLetter TEXT,
                                                                          FOREIGN KEY (JobID) REFERENCES JobListing(JobID),
                                                                          FOREIGN KEY (ApplicantID) REFERENCES Applicant(ApplicantID))'''
                self.execute(item)

                print("Database initialized successfully.")

    except Exception as e:
        print(f"Error during database initialization: {e}")

    finally:
        if conn:
            DBConnection.close(conn)