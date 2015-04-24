import pymongo
import sys


# Copyright 2013, 10gen, Inc.
# Author: Andrew Erlichson


# connnecto to the db on standard port
connection = pymongo.MongoClient("mongodb://localhost")


import pdb
db = connection.school                 # attach to db
collection = db.students         # specify the colllection

if __name__ == '__main__':
    students = collection.find({"scores.type":"homework"}, {"scores.type":1,"scores.score":1})
    studens_hw_scores = dict()
    for student in students:
        hw_scores = list()
        for score in student['scores']:
            if score['type']=="homework":
                hw_scores.append(score['score'])
        studens_hw_scores.update(dict([(str(student['_id']),sorted(hw_scores)[0])]))
        counter = 0
        for score in student['scores']:
            #print studens_hw_scores[student['_id']
            if score['score'] == studens_hw_scores[str(student['_id'])]:
                student['scores'].pop(counter)
            counter = counter + 1
        collection.save(student)