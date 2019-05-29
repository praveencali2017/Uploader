import os
ROOT_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_DIR=os.path.join(ROOT_DIR,'static','uploads')
HOST='0.0.0.0'
PORT=8000
SECRET_KEY ='testing123'

print(UPLOAD_DIR)