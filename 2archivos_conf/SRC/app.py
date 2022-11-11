import os
from dotenv import load_dotenv, find_dotenv

'''
from dotenv import load_dotenv, find_dotenv
load_dotenv (find_dotenv())
print(os.getenv('POSTGRESQL_HOST'))
print(os.getenv('POSTGRESQL_PORT'))
print(os.getenv('POSTGRESQL_USER'))
print(os.getenv('POSTGRESQL_PASSWORD'))

from decouple import config
print('Host: {HOST} - Puerto:{PORT}'.format(HOST=config('POSTGRESQL_HOST'),
PORT=config('POSTGRESQL_PORT')))
'''

load_dotenv (find_dotenv())
print(os.getenv('POSTGRESQL_HOST'))
print(os.getenv('POSTGRESQL_PORT'))
print(os.getenv('POSTGRESQL_USER'))
print(os.getenv('POSTGRESQL_PASSWORD'))