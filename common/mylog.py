
import logging
from common.myconf import myconf
import os
from common.constant import LOG_DIR
#读取配置项，设为全局变量
mylog_level = myconf.get('log','mylog_level')
f_level = myconf.get('log','f_level')
s_level = myconf.get('log','s_level')
filename = myconf.get('log','filename')
file_path = os.path.join(LOG_DIR,filename)
class MyLog(object):

    def __new__(cls, *args, **kwargs):
        my_log = logging.getLogger('my_log')
        # 创建日志收集渠道
        my_log.setLevel(mylog_level)

        # 创建日志本地输出渠道
        sh = logging.StreamHandler()
        sh.setLevel(s_level)

        # 创建日志文件输出渠道
        fh = logging.FileHandler(file_path, mode='a', encoding='utf8')
        fh.setLevel(f_level)

        # 将输出渠道添加到收集器中
        my_log.addHandler(sh)
        my_log.addHandler(fh)

        # 指定日志输出的格式
        fot = '%(asctime)s - [%(filename)s --> line:%(lineno)d] - %(levelname)s: %(message)s'

        # 创建日志格式对象
        formatter = logging.Formatter(fot)
        # 输出格式绑定到输出渠道上
        sh.setFormatter(formatter)
        fh.setFormatter(formatter)
        return my_log
my_log =MyLog()
my_log.info('-----------开始启动测试用例----------')
