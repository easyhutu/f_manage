"""
CREATE: 2018/5/26
AUTHOR:　HEHAHUTU
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

    def get_folder_id(self):
        data = {'folder_name': 'tests', 'assess_key': self.assess_key, 'folder_path': '/tests', 'group_id': 0}
        html = self.post_json('/x/folder/add', data)
        print(html.json)
        return html.json['data']['id']

    def test_create_folder(self):
        data = {'folder_name': 'tests', 'assess_key': self.assess_key, 'folder_path': '/tests', 'group_id': 0}
        html = self.post_json('/x/folder/add', data)
        print(html.json)
        self.assertEqual(0, html.json['code'])

    def test_update_folder(self):
        data = {'folder_name': 'aaa', 'assess_key': self.assess_key, 'id': 1}
        html = self.post_json('/x/folder/update', data)
        print(html.json)
        self.assertEqual(0, html.json['code'])

    def test_delete_folder(self):
        data = {'id': self.get_folder_id()}
        html = self.post_json('/x/folder/delete', data)
        print(html.json)
        self.assertEqual(0, html.json['code'])
