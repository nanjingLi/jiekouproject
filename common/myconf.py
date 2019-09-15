from configparser import ConfigParser
import os
from common.constant import CONF_DIR
config_file = os.path.join(CONF_DIR,'config.ini')
#封装成类
class MyConfig(ConfigParser):
    def __init__(self):
        super().__init__()
        self.read(config_file)
myconf = MyConfig()
#封装成函数
def myConfig():
    conf = ConfigParser()
    conf.read(config_file)
    return conf
