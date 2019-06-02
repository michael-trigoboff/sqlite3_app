import db, pcc.gui, sys

def update():
	if nStudents <= 1:
		wn.setEnabled('Prev', False)
		wn.setEnabled('Next', False)
	elif studentIndex == 0:
		wn.setEnabled('Prev', False)
		wn.setEnabled('Next', True)
	elif studentIndex == nStudents - 1:
		wn.setEnabled('Prev', True)
		wn.setEnabled('Next', False)
	else:
		wn.setEnabled('Prev', True)
		wn.setEnabled('Next', True)

def keypress(key):
	if key == 'Escape':
		wn.close()
	elif key == 'Return':
		wn.focusReturnKey()

def displayStudent():
	wn.setValue('Name',		students[studentIndex][0])
	wn.setValue('Credits',	students[studentIndex][1])
	wn.setValue('GPA',		students[studentIndex][2])

def btnClick(name):
	global studentIndex
	if name == 'Prev':
		studentIndex = studentIndex - 1
	else:	# name == 'Next'
		studentIndex = studentIndex + 1
	displayStudent()
	update()

def run(fileName):
	global nStudents, studentIndex, students, wn
	wn = pcc.gui.window.newWindow('Students', keypress, update)

	wn.addTextField('Name', enabled=False)
	wn.addTextField('Credits', enabled=False)
	wn.addTextField('GPA', enabled=False)

	wn.addButton('Prev', btnClick)
	wn.addButton('Next', btnClick, sameRow=True)

	if fileName is not None:
		db.load(fileName)
	else:
		db.connect(':memory:')
		db.createTable()
	students = db.getStudents()[1]
	nStudents = len(students)
	if nStudents > 0:
		studentIndex = 0
		displayStudent()
	update()

	wn.setPosn(300, 300)
	wn.open()

if len(sys.argv) == 2:
	run(sys.argv[1])
else:
	run(None)