import os
"""
常量模块，获取项目项目目录的路径，保存
项目路径
用例类所在路径
配置文件的路径
用例数据的路径
日志文件的路径
测试报告的路径 
"""
#项目目录
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#测试用例目录
CASES_DIR = os.path.join(BASE_DIR,'testcases')
#配置文件目录
CONF_DIR = os.path.join(BASE_DIR,'conf')
#用例数据目录
DATA_DIR = os.path.join(BASE_DIR,'data')
#日志文件目录
LOG_DIR = os.path.join(BASE_DIR,'logs')
#测试报告目录
REPORT_DIR = os.path.join(BASE_DIR,'reports')

