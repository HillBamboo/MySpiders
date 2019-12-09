import os

from pymongo import MongoClient
from pymongo.database import Database
from gridfs import GridFS

client = MongoClient('localhost', 27017)
db = client.xxd_imgs

ROOT_DST = './pics'
gdf = GridFS(db, collection='fs')
cnt = 0
for i, out in enumerate(gdf.find()):
    cnt += 1
    img_data = out.read()
    with open(f'{i}.jpeg', 'wb') as img_file:
        img_file.write(img_data)
