import MySQLdb
import logging

# Inherit logging
logger = logging.getLogger('root')


class mydb(object):
    def __init__(self, user, password, host, database):
        try:
            self.mydb_cnx = MySQLdb.connect(user=user, passwd=password,
                                            host=host, db=database)
            self.mydb_cursor = self.mydb_cnx.cursor()

        except Exception as e:
            logging.error("mydb: __init__: exception: %s" % e)

    def close(self):
        self.mydb_cnx.close()

    def exec_sql(self, sql):
        try:
            # TODO more injection protection
            if sql[-1] != ';':
                sql = sql + ';'
            logging.debug("mydb: exec_sql: SQL statement: \n%s" % sql)
            self.mydb_cursor.execute(sql)
            return self.mydb_cursor.fetchall()
        except Exception as e:
            logging.debug("mydb: exec_sql: exception: %s" % e)
            return None
