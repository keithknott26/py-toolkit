#PDB - Python DeBugger
import pdb

#set_trace() breaks the execution while running
pdb.set_trace()

#pdf is a python module, and NOT a separate process
#set_trace() kick starts the debugger

print "Started..."
for i in range(0,100):
	print i
print "Complete..."

#start the script under pdb
#python -m pdb script.py

#in pdb mode, to interrupt the program execution, press
#ctrl + c

#to resume execution after hitting a breakpoint or interrupting 
# via ctrl + c, press c which continues the program flow
#until it hits the next breakpoint

#to exit pdb, enter quit