"""
Author: Meng
Date: 2018/6/2
"""
from flask import url_for
from flask_testing import LiveServerTestCase, TestCase
from app import create_app
import unittest
import json
import requests
import time


class FolderTest(TestCase):
    header = {'Content-Type': 'application/json;charset=utf-8'}

    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8943
        app.config['LIVESERVER_TIMEOUT'] = 10
        # self.clent = app.test_client()
        return app

    def post_json(self, path, data):
        endata = json.dumps(data)
        html = self.client.post(path, data=endata, headers=self.header, follow_redirects=True)
        return html

    def tearDown(self):
        # mongo.db.task.remove()
        pass

    def setUp(self):
        self.assess_key = self.post_json('/x/login', data={'username': 'meng', 'password': '123456'}).json['data'][
            'assess_key']
        pass

    def test_create_config(self):
        data = dict(
            server_name='f_cloud',
            is_register=1,
            default_reg_role='NORMAL',
            assess_key=self.assess_key
        )
        html = self.post_json('/x/config', data)
        print(html.json)
