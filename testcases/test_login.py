"""
测试用例模块
"""
import unittest
from pack_lib.ddt import ddt,data
from common.my_read_excel import readExcel
from common.my_requests import HttpRequest
from common.mylog import my_log
from common.constant import DATA_DIR
from common.my_mysql import ReadSQL
import os
workbook = os.path.join(DATA_DIR,'cases2.xlsx')
@ddt
class LoginTestCase(unittest.TestCase):
    """登陆接口"""
    excel = readExcel(workbook,'Login')
    cases = excel.read_data_obj()
    @data(*cases)
    def test_cases_login(self,case):
        #入参
        url = case.url
        data = eval(case.data)
        method = case.method
        code_id = case.code_id + 1
        http = HttpRequest(method=method,url=url,data=data)
        #期望值
        excepeted = eval(case.excepted)
        #发送请求到接口，获取接口实际值
        response =http.httpRequest().json()
        #比较实际结果和预期结果，断言用例是否通过
        try:
            self.assertEqual(response,excepeted)
        except AssertionError as e:
            self.excel.write(row=code_id,column=8,value="不通过")
            my_log.debug("{},该条用例执行未通过".format(case.title))
            #my_log.error(e)
            raise e
        else:
            self.excel.write(row=code_id,column= 8,value= "通过")
            my_log.debug("{},该条用例执行通过".format(case.title))

@ddt
class RegisterTestCase(unittest.TestCase):
    """注册接口"""
    excel = readExcel(workbook,'register')
    cases = excel.read_data_obj()
    db = ReadSQL()
    global resk
    @data(*cases)
    def test_cases_register(self,case):
        # 入参
        url = case.url
        data = eval(case.data)
        method = case.method
        code_id = case.code_id + 1
        http = HttpRequest(method=method,url=url,data=data)
        # 期望值
        excepted = eval(case.excepted)
        # 发送请求到接口，获取接口实际值
        response = http.httpRequest().json()
        #判断是否需要进行sql校验

        # 比较实际结果和预期结果，断言用例是否通过
        try:
            self.assertEqual(response, excepted)
            if case.check_sql:
                resk = self.db.find_count(case.check_sql)
                self.assertEqual(1,resk)
        except AssertionError as e:
            self.excel.write(row=code_id, column=8, value="不通过")
            my_log.debug("{},该条用例执行未通过".format(case.title))
            # my_log.error(e)
            my_log.exception(e)
            raise e
        else:
            self.excel.write(row=code_id, column=8, value="通过")
            my_log.debug("{},该条用例执行通过".format(case.title))


