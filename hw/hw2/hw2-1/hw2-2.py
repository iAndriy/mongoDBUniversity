import pymongo
import sys


# Copyright 2013, 10gen, Inc.
# Author: Andrew Erlichson


# connnecto to the db on standard port
connection = pymongo.MongoClient("mongodb://localhost")


import pdb
db = connection.students                 # attach to db
collection = db.grades         # specify the colllection
if __name__ == '__main__':
	x = collection.find()
	x.find({"type":"homework"})
	pdb.set_trace()	
	print x.next()
