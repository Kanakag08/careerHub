class Company(DBCConnection):
    def create(self):
        item='''create table if not exists company(companyID int primary key,
                                                   companyName varchar(50),
                                                   location varchar(60))'''
        self.execute(item)
