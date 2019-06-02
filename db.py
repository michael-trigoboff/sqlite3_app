import sqlite3

def connect(dbName):
	global conn, crsr
	conn = sqlite3.connect(dbName)
	crsr = conn.cursor()

def load(fileName):
	global conn, crsr
	conn.close()
	conn = sqlite3.connect(':memory:')
	f = open(fileName, 'r')
	sql = f.read()
	f.close()
	conn.executescript(sql)
	crsr = conn.cursor()

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
	crsr.execute('SELECT * FROM students')
	return crsr.fetchall()

def close():
	conn.commit()
	conn.close()

