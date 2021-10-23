#Post a iterm2 notification using growl 
def growl_notify(code):
    #print "Notify:" + "printf '\\e]9;" + code + "\\a'"
    os.system("printf '\\e]9;" + code + "\\a'")