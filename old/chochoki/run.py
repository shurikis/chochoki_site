import os

# settings
import sys

ip = '127.0.0.1'  # default: '127.0.0.1'
port = 8000  # default: 8000

# run
if len(sys.argv) >= 2: ip = sys.argv[1]
if len(sys.argv) >= 3: ip = sys.argv[2]
os.system(f'python3 manage.py runserver {ip}:{port}')
