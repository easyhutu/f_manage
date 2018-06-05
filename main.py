"""
CREAT: 2017/12/9
AUTHOR:　HEHAHUTU
"""

from app import create_app

app = create_app()

from lib.celerys import make_celery


f_celery = make_celery(app)

if __name__ == '__main__':
    app.run(port=5000)
