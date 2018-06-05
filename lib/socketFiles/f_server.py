"""
Author: Meng
Date: 2018/6/3
"""
from socketserver import TCPServer, BaseRequestHandler
import threading
import os
from lib.Serialization import value_loads
import json


class EchoHandler(BaseRequestHandler):

    def handle(self):
        print('Got connection from', self.client_address)
        # self.rfile is a file-like object for reading
        # for line in self.rfile:
        #     # self.wfile is a file-like object for writing
        #     self.wfile.write(line)

        while True:

            msg = self.request.recv(8192)
            if not msg:
                break

            try:
                value = value_loads(msg.decode())
                if value:
                    print(value)
                    base_path = value['base_path']
                    data = bytes(value['data'])
                    filename = value['filename']
                    print(base_path)
                    path = os.path.join(base_path, filename)
                    with open(path, 'wb') as f:
                        f.write(data)

                    print(path)
                    m = {'code': 100, 'msg': 'save file success', 'filename': filename}
                    self.request.send(json.dumps(m).encode())

            except:
                m = {'code': 500, 'msg': 'save failed'}
                self.request.send(json.dumps(m).encode())


class SServer:
    def __init__(self, ip='', port=8899, work_num=20):

        self.ip = ip
        self.port = port
        self.work_num = work_num

    def run(self):
        th = []
        serv = TCPServer((self.ip, self.port), EchoHandler)
        for num in range(self.work_num):
            worker = threading.Thread(target=serv.serve_forever)
            worker.daemon = True
            th.append(worker)

        for work in th:
            print('new socket {}'.format(work.name))
            work.start()

        serv.serve_forever()


if __name__ == '__main__':
    ss = SServer()
    ss.run()
