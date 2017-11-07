from flask_script import Manager
from songbase import app

manager = Manager(app)   ##create a manager that manages app

if __name__ == '__main__':
    manager.run()
