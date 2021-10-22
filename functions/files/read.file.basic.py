"""Snippets for various ways to read files"""

"""The file to read"""
FILE_PATH = '/tmp/fb_ads.csv'

### Basic opening a file for reading ###
# Open the file
with open(FILE_PATH) as read_file:
    # iterate over the lines of the file
    for line in read_file.readlines():
        print(line)



### Snippet for reading with the fileinput module ###
# Iterate over the lines in files.
# fileinput can take either a single filename or a list of them.
# if given a list it will loop over the lines in all of them in the order given.
for line in fileinput.input(FILE_PATH):
    # fileinput has useful utility functions
    
    # first line in current file?
    if fileinput.isfirstline():
        # Get the filename of the current file
        file_name = fileinput.filename()
        print('First line of %s' % file_name)

    # line number in current file
    file_line_no = fileinput.filelineno()
    # line number in all read lines
    line_no = fileinput.lineno()
    print('(%s in file, %s total) - %s' % (file_line_no, line_no, line))
    
# fileinput needs to be closed after use        
fileinput.close()
