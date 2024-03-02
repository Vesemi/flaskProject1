import os

os.system('flask db init')
os.system('flask db migrate')
os.system('flask db upgrade')