from RepositoryDataBase.RepositoryDataBase import Repository


class blCar():

    def Add(self, User,Pass):

        repos = Repository()
        return repos.insert_user_pass_data(User,Pass)


    def Read(self, tblname, col):
        repos = Repository()
        return repos.Read(tblname, col)

    def Read_Sort(self, tblname, col, field):
        repos = Repository()
        return repos.Read_Sort(tblname, col, field)

    def Create(self, obj):
        repos = Repository()
        return repos.CreateTable(obj)

    def Insert(self, obj, Tablename, Cols):
        repos = Repository()
        return repos.Insert(obj, Tablename, Cols)