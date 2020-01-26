from cryptography.fernet import Fernet
import os
import pymongo

key = os.environ['ENCRYPTION_KEY']
f = Fernet(key)


db_creds = f.decrypt(b'gAAAAABeLd-DheaVqD_15wWvY6__IVbOqL_8AET6_owd8DlNrEqliZWi9fv5pw9HiSV_'
                        b'mm3PRDNBvoVNvAazEa8ahssinIPxY6aR8yvF36oyta4X7cueLGw=').decode()
db_server = f.decrypt(b'gAAAAABeLd_utpFYHTz2knY4ryz4ZdbUt8fWpL8W063HyZ2lWVWdKKp4QZlxw1wsGPpm'
                           b'6E3Sh2hljfxdAh9Yx7mVyOmNtxGC_Dxg-VUphjxVk73tiz7YIFo=').decode()
db_name = 'test'
print('Attempting to connect to Server...')
client = pymongo.MongoClient("mongodb+srv://{0}@{1}/{2}?retryWrites=true&w=majority".
                             format(db_creds, db_server, db_name))
print('Connection was successfully established!')
Session = client.test
