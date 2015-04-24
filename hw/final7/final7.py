import pymongo
import sys


# Copyright 2013, 10gen, Inc.
# Author: Andrew Erlichson


# connnecto to the db on standard port
connection = pymongo.MongoClient("mongodb://localhost")


import pdb
db = connection.test                 # attach to db
images = db.images			# specify the colllection
albums = db.albums	         
if __name__ == '__main__':
	for image in images.find():
		al_count = albums.find({'images':{'$in':[image['_id']]}}).count()
		if not al_count:
			images.remove(image)
	print images.count()
