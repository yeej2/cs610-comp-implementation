#!/usr/bin/env python

# Date 9 April 2018
# pymongo demo

# Inspiration of the source code (3 April 2018):
# ref: https://codehandbook.org/pymongo-tutorial-crud-operation-mongodb/

# to run this code, we must first establish a data directory, start up the mongod server
# Commands:
# Make the data directory
# mkdir ~/mondoDbData
# Run the MongoDB server
# . mongod --dbpath ~/mondoDbData
# ./pymongoWithPython_ii.py

from pymongo import MongoClient
import string
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(TEST)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

# creating connectioons for communicating with Mongo DB
client = MongoClient('localhost:27017')

db = client.STUDENTS # the name of the database in mongo. this base may be found by the command, "show dbs" in mongo



def begin():
# driver method for the program
    print("  The agents database for use with MongoDB.")
    print("  Uses the pymongo client")
    while(1):
	# choose an option to select a dataStudent operation
        selection = raw_input('\n Select: 0 for DB information,\n\t 1 to insert,\n\t 2 to update,\n\t 3 to read,\n\t 4 to delete or,\n\t q to Quit\n\t : ')

        if selection == '0':
            info()
        elif selection == '1':
            insert()
    	elif selection == '2':
            update()
    	elif selection == '3':
            read()
    	elif selection == '4':
            print 'delete'
            delete()
        elif string.upper(selection) == 'Q':
            print " Exiting ... ",
            exit()
    	else:
	    print '\n INVALID SELECTION \n'
# end of begin()



def info():
# Function to get some information about the dataStudent itself.
    print " Information about the students."
    try:
        result = db.Students.db
        print '\n Info: ',result

    except Exception, e:
        print str(e)

# end of info()



def insert():
# Function to insert data into mongo db
    try:
	studentId = raw_input('Enter Student id :')
	studentFirstName = raw_input('Enter FirstName :')
	studentLastName = raw_input('Enter LastName :')
	studentAge = raw_input('Enter age :')
	studentCountry = raw_input('Enter Country :')

# insert the data into the base
	db.Student.insert_one(
	    {
		"id": studentId,
	        "FirstName":studentFirstName,
		"LastName":studentLastName,
		"age":studentAge,
		"country":studentCountry
	    })
        print '\nInserted data successfully\n'

    except Exception, e:
        print str(e)
# end of insert()



def update():
# Function to update record to mongo db
    print "  Update:"
    try:

	studentId = raw_input('  Enter Student id :')
	studentFirstName = raw_input('  Enter FirstName :')
	studentLastName = raw_input('  Enter LastName :')
	studentAge = raw_input('  Enter age :')
	studentCountry = raw_input('  Enter Country :')


# update the record with the new information
	db.Student.update_one(
	    {"id": studentId},
	    {
		"$set": {
		    "firstName":studentFirstName,
		    "lastName":studentLastName,
		    "age":studentAge,
		    "country":studentCountry
		}
	    }
	)
	print "\nRecords updated successfully. \n"
    except Exception, e:
	print str(e)
# end of update()



def read():
# function to read records from mongo db
    try:
	empCol = db.Student.find()
	print '\n Found: all data from DataStudent \n'
	for emp in empCol:
	    print emp
    except Exception, e:
	print str(e)
# end of read()



# Function to delete record from mongo db
def delete():
    try:
	studentId = raw_input('\nEnter student id to delete\n')
        db.Student.delete_many({"id":studentId})
	print '\nDeletion successful\n'
    except Exception, e:
	print str(e)
#end of deltete()


begin() # start up the program: call the main function to begin
