import os

from pymongo import MongoClient
from pymongo.database import Database
from gridfs import GridFS

# db_client = Database(client, name='abc')
# db_client.create_collection(name="abc_imgs")

client = MongoClient('localhost', 27017)
db = client.abc_imgs

ROOT_IMGS = './pics'
for file in os.listdir(ROOT_IMGS):
    fname, fext = file.split('.')
    with open(os.path.join(ROOT_IMGS, file), 'rb') as img_data:
        writer = GridFS(db)
        writer.put(img_data, content_type=fext, filename=fname)
print('insert OK')