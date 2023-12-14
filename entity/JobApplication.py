# job Application class
class JobApplication(DBConnection):
    def create(self):

        item='''Create table if not exists JobApplication(ApplicationID INT PRIMARY KEY,
                                                          JobID INT,
                                                          ApplicantID INT,
                                                          ApplicationDate DATETIME,
                                                          CoverLetter TEXT,
                                                          FOREIGN KEY (JobID) REFERENCES JobListing(JobID),
                                                          FOREIGN KEY (ApplicantID) REFERENCES Applicant(ApplicantID))'''
        self.execute(item)