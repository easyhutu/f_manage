"""
CREATE: 2018/5/6
AUTHOR:　HEHAHUTU
"""
from app import create_app
from flask_migrate import MigrateCommand
from flask_script import Manager


app = create_app()
manage = Manager(app)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()
