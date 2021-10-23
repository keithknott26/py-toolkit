#Raising an exception is to interrupt program flow
#Handling an exception is to resume control
#unhandled exceptions are caused when a exception propogates to the start of the call stack will cause the program to terminate
#In python empty blocks aren't allowed, which will raise an IndentationError.
#-- If you need empty blocks you can use the keyword 'pass' which is a no-ops
#Programmer errors like IndentationError, SyntaxError and NameError NOT be caught
#raise keword simply reraises the expcetion


def add_num(fno, sno):
	val = 0
	try:
		val = fno +  sno
	#This handles multiple exceptions of type ValueError and TypError
	except(ValueError, TypeError) as e:
		print("Add operation failed!: " + str(e))
	#catch all other exceptions. Exception info will
	except:
		print "Unknown error occured"
		raise
	finally:
		print "Finally block is executed irrespetive of the error"
	return val

#pass demo, here if the pass keyword isn't specified will endup
a = 10
if a == 10:
	pass

#IndexError - When index is out of range for lists
#KeyError - When a key doesn't exist in dictionary
#ValueError - Whan an object is of the right type but contains an inappropriate value
#In Python its NOT to do Type checking like if checking for int for add operation

#Pythonic error handling philosophies (Favours EAFP)
#Look Before You Leap - LBYL
#Example:
#---------------------------------
#If file exists
#	Then read file
#---------------------------------
#The problem with this approach is, what if a file gets deleted the moment
#its about to access (Race Conditions)

#Its Easier to Ask Forgieness than Permission - EAFP + Exceptions
#THis is the recommend way in Python
#Example
#try:
#	readFile
#except:
#Here the operation is carried out without checks,and exceptions are cought