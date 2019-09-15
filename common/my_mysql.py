"""
为什么要封装？
方便使用

封装的需求是什么？
逻辑代码封装成方法，关键数据参数化处理
"""
import pymysql
from common.myconf import myconf
class ReadSQL(object):
    def __init__(self):
        pass
        #建立连接
        self.connect = pymysql.connect(host=myconf.get('mysql','host'),
                                  port=myconf.getint('mysql','port'),
                                  user=myconf.get('mysql','user'),
                                  password=myconf.get('mysql','password'),
                                  database=myconf.get('mysql','database'))
        # 创建游标
        self.cursor = self.connect.cursor()
    def close(self):
        #关闭游标，再断开连接
        self.cursor.close()
        self.connect.close()
    def find_one(self,sql):
        """返回一条语句"""
        self.cursor.execute(sql)
        return self.cursor.fetchone()
    def find_all(self,sql):
        """返回sql语句查询到的所有结果"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    def find_count(self,sql):
        self.connect.commit()
        count=self.cursor.execute(sql)
        return count
if __name__ == '__main__':
    sql = "select *  from member where MobilePhone='18999990252'"
    sql2 = "select * from member LIMIT 0,5"
    db=ReadSQL()
    res = db.find_all(sql2)
    print(res)