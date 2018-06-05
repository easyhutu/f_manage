"""
Author: Meng
Date: 2018/6/3
"""
from socket import *
import os
import json
from lib.Serialization import value_dump


class SClient:
    def __init__(self, assess_key, file_path, save_base_path, ip, port=8899, ):
        self.ip = ip
        self.port = port
        self.path = file_path
        self.base_path = save_base_path
        self.assess_key = assess_key

    def _read_file(self):
        with open(self.path, 'rb') as f:
            data = f.read()
        filename = os.path.split(self.path)[-1]

        value_dict = dict(
            filename=filename,
            data_type='bytes',
            base_path=self.base_path,
            assess_key=self.assess_key,
            data=str(data),
        )
        value = json.dumps(value_dict).encode()
        return value

    def send_file(self):
        so = socket(AF_INET, SOCK_STREAM)
        so.connect((self.ip, self.port))
        so.send(self._read_file())
        rev = so.recv(4096)
        print(rev)


if __name__ == '__main__':
    fs = SClient(file_path='C:\\userFiles\\pro\\f_manage\\TIM2.2.0.exe',
                 save_base_path='C:\\userFiles\\pro\\f_manage\\lib\\socketFiles', assess_key='test', ip='127.0.0.1')
    fs.send_file()
