"""
Author: Meng
Date: 2018/6/7
"""
import psutil
import subprocess
import time
import argparse

start_uwsgi_cmd = '/opt/venv/bin/uwsgi --ini /opt/f_manage/uwsgi.ini'
pull_git = 'cd /opt/f_manage && git pull'


def kill_uwsgi_server():
    all_process = psutil.process_iter()
    uwsgi_pid = []
    for process in all_process:
        if 'uwsgi' in process.name():
            uwsgi_pid.append(process.pid)

    for p in uwsgi_pid:
        try:
            subprocess.call('kill -9 {}'.format(p), shell=True)
            print('kill pid: {}'.format(p))
        except Exception as e:
            print(e)


def arg_parse():
    parser = argparse.ArgumentParser(description="start python flask service")
    parser.add_argument('--pull', '-p', type=str, help='is git pull')
    parse = parser.parse_args()
    if str(parse.pull).lower() in ['yes', 'y', 'true']:
        return True
    return


if __name__ == '__main__':
    if arg_parse():
        subprocess.call(pull_git, shell=True)
    kill_uwsgi_server()
    time.sleep(2)
    subprocess.call(start_uwsgi_cmd, shell=True)
