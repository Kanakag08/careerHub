class SalaryCalculationException(Exception):
    pass

    def calculate_average_salary(JobListing):
        try:
            total_salary=0
            valid_JobListing=0

            for job in JobListing:
                if job['salary']<0:
                    raise SalaryCalculationException(job['JobTitle'])
                total_salary += job['salary']
                valid_JobListing += 1

            if valid_JobListing == 0:
                raise ZeroDivisionError("no valid job listing found with non- negavtive salary")

            average_salary= total_salary/valid_JobListing
            print(f"Average salary: {average_salary}")

        except SalaryCalculationException as e:
            print(f"Error occured salary can not br negative: {e}")

        except ZeroDivisionError as e:
            print(f"Error: {e}")