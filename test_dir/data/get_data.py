import jsonpath
import sys
import json
from os.path import dirname, abspath

base_path = dirname(dirname(abspath(__file__)))
sys.path.insert(0, base_path)


class GetData:

    def __init__(self, json_name, file_path=base_path + "/data/data_file.json"):
        """
        读取参数化文件
        :param json_name:json文件中待提取的数据模块名字
        :return:
        """
        with open(file_path, "r", encoding="utf-8") as fp:
            self.data = json.load(fp)[json_name]

    def get_value(self, key):
        """json获取key的values"""
        if isinstance(self.data, dict):
            values = jsonpath.jsonpath(self.data, '$..%s' % (key))
            return values
        else:
            values = jsonpath.jsonpath(self.data, '$..%s' % (key))
            return values
