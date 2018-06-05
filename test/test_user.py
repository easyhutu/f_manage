"""
CREAT: 2017/12/10
AUTHOR:　HEHAHUTU
"""

from flask import url_for
from flask_testing import LiveServerTestCase, TestCase
from app import create_app
import unittest
import json
import requests
import time


class UserTest(TestCase):
    header = {'Content-Type': 'application/json;charset=utf-8'}

    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8943
        app.config['LIVESERVER_TIMEOUT'] = 10
        # self.clent = app.test_client()
        return app

    def tearDown(self):
        # mongo.db.task.remove()
        pass

    def test_create_user(self):
        data = {'username': 'meng', 'email': 'test@qq.com', 'password': '123456'}
        endata = json.dumps(data)
        html = self.client.post('/x/user', data=endata,
                                headers=self.header, follow_redirects=True)
        print(html.json)

    def test_login(self):
        data = {'username': 'meng', 'email': 'test@qq.com', 'password': '123456'}
        endata = json.dumps(data)
        html = self.client.post('/x/login', data=endata,
                                headers=self.header, follow_redirects=True)
        print(html.json, html.headers)


if __name__ == '__main__':
    unittest.main()
