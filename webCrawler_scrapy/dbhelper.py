import MySQLdb
from scrapy.utils.project import get_project_settings

class DBHelper():
    
    def __init__(self):
        self.settings=get_project_settings()
        
        self.host=self.settings['MYSQL_HOST']
        self.port=self.settings['MYSQL_PORT']
        self.user=self.settings['MYSQL_USER']
        self.passwd=self.settings['MYSQL_PASSWD']
        self.db=self.settings['MYSQL_DBNAME']
    
    def connectMysql(self):
        conn=MySQLdb.connect(host=self.host,
                             port=self.port,
                             user=self.user,
                             passwd=self.passwd,
                             charset='utf8')
        return conn
    def connectDatabase(self):
        conn=MySQLdb.connect(host=self.host,
                             port=self.port,
                             user=self.user,
                             passwd=self.passwd,
                             db=self.db,
                             charset='utf8')
        return conn   
    
    def createDatabase(self):
        conn=self.connectMysql()
        
        sql="create database if not exists "+self.db
        cur=conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.close()
    
    def createTable(self,sql):
        conn=self.connectDatabase()
        
        cur=conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.close()
    def insert(self,sql,*params):
        conn=self.connectDatabase()
        
        cur=conn.cursor()
        cur.execute(sql,params)
        conn.commit()
        cur.close()
        conn.close()
    def update(self,sql,*params):
        conn=self.connectDatabase()
        
        cur=conn.cursor()
        cur.execute(sql,params)
        conn.commit()
        cur.close()
        conn.close()
    
    def delete(self,sql,*params):
        conn=self.connectDatabase()
        
        cur=conn.cursor()
        cur.execute(sql,params)
        conn.commit()
        cur.close()
        conn.close()
        
        

class TestDBHelper():
    def __init__(self):
        self.dbHelper=DBHelper()
        self.testCreateTable()

    def testCreateDatebase(self):
        self.dbHelper.createDatabase()

    def testCreateTable(self):

        sql="CREATE TABLE `weather` (  `id` int(11) NOT NULL AUTO_INCREMENT,  `date` varchar(50) COLLATE utf8_bin DEFAULT NULL,  `max_tempe` varchar(50) COLLATE utf8_bin DEFAULT NULL,  `min_tempe` varchar(50) COLLATE utf8_bin DEFAULT NULL,  `weather` varchar(100) COLLATE utf8_bin DEFAULT NULL,  `wind` varchar(50) COLLATE utf8_bin DEFAULT NULL,  `wind_power` varchar(50) COLLATE utf8_bin DEFAULT NULL,  `address` varchar(100) COLLATE utf8_bin DEFAULT NULL,  `address_code` varchar(100) COLLATE utf8_bin DEFAULT NULL,  PRIMARY KEY (`id`) USING BTREE,  UNIQUE KEY `idx_date` (`date`,`address_code`) USING BTREE) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;"

        self.dbHelper.createTable(sql)
        print "create table completed ."


if __name__=="__main__":
    testDBHelper=TestDBHelper()
