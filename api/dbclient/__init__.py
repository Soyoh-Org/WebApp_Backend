from cryptography.fernet import Fernet
import os
import pymongo

key = os.environ['ENCRYPTION_KEY']
f = Fernet(key)
mongodb_pwd = f.decrypt(b'gAAAAABeLR1H3kdgWujknAuTDqPBtv8UMaseRn0FM2MNQrBTQ8Wgbx_'
                        b'3IqcnsIT76tim45DidkzWyG3vmbCqkhJ0pKwKELgC30xE0Wxn_PK45Z4erUX6h7Q=').decode()
mongodb_server = f.decrypt(b'gAAAAABeLSCzIkJvoqsc5J01Bl_JCEcriPJ7ZA0eX9uaKf5k7Si-2qw0euNpsJx'
                           b'86vIZ6pGw2BlT_F4qGEjQKfzMXiVcPE-rcNV6kaqd17iC4lDKxjPI2i0=').decode()
client = pymongo.MongoClient("mongodb+srv://root:{0}@{1}/test?retryWrites=true&w=majority".
                             format(mongodb_pwd, mongodb_server))
db = client.test
collection = db.test

for x in collection.find():
    print(x['name'])
