class ApplicationDeadlineException(Exception):
    pass

    def submit_job_application(JobApplication):
        try:
            if JobApplication.ApplicationDate > ApplicationDeadline:
                raise ApplicationDeadlineException()
            print("Job application submited succesfully")

        except ApplicationDeadlineException as e:
            print(f"Error: {e}")