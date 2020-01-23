import db, sys

quitRequested = False

def addFn(cmd):
	if len(cmd) != 4:
		print('add command needs: name, credits, gpa')
		return
	sqlStr = db.addStudent(cmd[1], cmd[2], cmd[3])
	print(sqlStr)

def deleteFn(cmd):
	if len(cmd) != 2:
		print('delete command needs: student name')
		return
	sqlStr = db.deleteStudent(cmd[1])
	print(sqlStr)

def helpFn(cmd):
	for cmdInfo in cmds.items():
		cmdName = cmdInfo[0] + ':'
		print(f'{cmdName:10}{cmdInfo[1][1]:}')

def loadFn(cmd):
	if len(cmd) != 2:
		print('load command needs: file name')
		return
	db.load(cmd[1])

def printFn(cmd):
	sqlStr, students = db.getStudents()
	print(sqlStr + '\n')
	if len(students) == 0:
		print('-- no students --')
	else:
		hdrFormatStr = '{:10} {:>7} {:>8}'
		print(hdrFormatStr.format('name', 'credits', 'gpa'))
		print(hdrFormatStr.format('----', '-------', '----'))
		for student in students:
			print(f'{student[0][:10]:10} {student[1]:7} {student[2]:8.2f}')
	print()

def quitFn(cmd):
	global quitRequested
	quitRequested = True

def storeFn(cmd):
	if len(cmd) != 2:
		print('store command needs: file name')
		return
	db.store(cmd[1])

cmds = {
	'add':		(addFn, 	'add a student to the database'),
	'delete':	(deleteFn,	'delete a student from the database'),
	'help':		(helpFn,	'print command documentation'),
	'load':		(loadFn,	'load a database file'),
	'print':	(printFn,	'print the students'),
	'quit': 	(quitFn,	'quit the app'),
	'store': 	(storeFn,	'store a database file')
}

def run(fileName):
	if fileName is not None:
		db.load(fileName)
	else:
		db.connect(':memory:')
		db.createTable()
	while not quitRequested:
		try:
			line = input('> ')
			if line == '':
				continue
			cmd = line.split()
			cmds[cmd[0]][0](cmd)
		except KeyError:
			print(f'{cmd[0]:} is not a command')
		except Exception as e:
			print(f"{cmd[0]} command failed with '{e:}'")
	db.close()

if __name__ == '__main__':
	if len(sys.argv) == 2:
		run(sys.argv[1])
	else:
		run(None)