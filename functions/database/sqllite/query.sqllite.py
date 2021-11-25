import sqllite3

class Database1:

    def get_connection(self, host, port, db, user='', password=''):
        pass

    def execute(self, conn, sql, params, unescaped=None):
        pass


class MysqlDatabase(Database1):
    def get_connection(self, host, port='', db='', user='', password=''):
        return MySQLdb.connect(password=password, host=host, port=port, db=db, user=user)

    def execute(self, conn, sql, params, unescaped=None):
        return conn.execute(sql, params)


class SqlLite3(Database1):
    def get_connection(self, host, port='', db='', user='', password=''):
        return sqlite3.connect(host)

    def execute(self, conn, sql, params, unescaped=None):
        sql = sql.format(unescaped) if unescaped else sql
        try:
            if params:
                return conn.cursor().execute(sql, params)
            else:
                return conn.cursor().execute(sql)
        finally:
            conn.commit()


class DatabaseFactory:
    def get_db(self) -> Database1:
        pass
    

class MysqlFactory(DatabaseFactory):
    def get_db(self) -> Database1:
        return MysqlDatabase
    
    
class SqlLiteFactory(DatabaseFactory):
    def get_db(self) -> Database1:
        return SqlLite3