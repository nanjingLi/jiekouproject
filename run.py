"""
项目启动文件
"""
import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from common.mylog import my_log
from common.constant import REPORT_DIR,CASES_DIR
import os
report_file= os.path.join(REPORT_DIR,'resport.html')

#第一步创建测试套件
my_log.info('-----------开始启动测试用例----------')
suite = unittest.TestSuite()
#第二步：将用例添加到套件
loader = unittest.TestLoader()
suite.addTest(loader.discover(CASES_DIR))
#第三步：执行用例，生成测试报告
with open(report_file,'wb') as fb:
    runner = HTMLTestRunner(stream=fb,
                            verbosity=2,
                            title='测试报告',
                            description='描述内容',
                            tester='南京阿良'

    )
    runner.run(suite)
my_log.info('----------该次所有用例执行完毕--------------')
