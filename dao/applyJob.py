from util.DBConnection import DBConnection

def applyJob(self):
    try:
        ApplicantID = int(input("Enter the Applicant ID: "))
        coverLetter = input("Enter Cover Letter: ")
        item = f'''insert into JobListing values({ApplicantID},'{coverLetter}')'''
        self.execute(item)
    except Exception as e:
        print(f"Error: {e}")