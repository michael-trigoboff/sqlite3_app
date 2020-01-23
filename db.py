import sqlite3

dbOpen = False

def connect(dbName):
	global dbOpen, conn, crsr
	conn = sqlite3.connect(dbName)
	crsr = conn.cursor()
	dbOpen = True

def load(fileName):
	global dbOpen, conn, crsr
	if dbOpen:
		conn.close()
		dbOpen = False		# set in case connect fails
	conn = sqlite3.connect(':memory:')
	f = open(fileName, 'r')
	sql = f.read()
	f.close()
	conn.executescript(sql)
	crsr = conn.cursor()
	dbOpen = True

def store(fileName):
	f = open(fileName, 'w')
	for line in conn.iterdump():
		print(line, file=f)
	f.close()

def createTable():
	sqlStr = 'CREATE TABLE students (name TEXT, credits INTEGER, gpa REAL)'
	crsr.execute(sqlStr)
	return sqlStr

def addStudent(name, credits, gpa):
	sqlStr = f"INSERT INTO students (name, credits, gpa) VALUES ('{name:}', '{credits:}', '{gpa:}')"
	crsr.execute(sqlStr)
	return sqlStr

def deleteStudent(name):
	sqlStr = f"DELETE FROM students WHERE name = '{name:}'"
	crsr.execute(sqlStr)
	return sqlStr

def getStudents():
	sqlStr = 'SELECT * FROM students'
	crsr.execute(sqlStr)
	return (sqlStr, crsr.fetchall())

def close():
	global dbOpen
	conn.commit()
	conn.close()
	dbOpen = False

