def condense_lines(lines=[]):
    output = ""

    #Types of logs
    al_log=0
    a7_log=0

    #print(str(lines))

    #Check x number of lines
    if len(lines) >= 250:
        lines_to_check = 250
    elif len(lines) > 0 and len(lines) < 250:
        lines_to_check = len(lines)
    else:
        if debug:
            print(warnStr, "\ncondense_lines(): Error - Empty list provided as input.")
        return

    #Identify which log type this is
    for line in lines[:lines_to_check]: 
        if re.match('^[0-9][0-9][0-9][0-9]\.[0-9][0-9]\.[0-9][0-9]\s[0-9][0-9]:[0-9][0-9]:[0-9][0-9],[0-9]{1,3}',line):
            al_log = 1
            break
        elif re.match('^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]\s[0-9][0-9]:[0-9][0-9]:[0-9][0-9],[0-9]{1,3}',line): 
            a7_log = 1
            break

    if not a7_log and not al_log:
        print(warnStr, "condense_lines(): Error - First " + str(lines_to_check) + " line(s) didn't match date regex.")
        return

    for i in range(len(lines)):
        no_tabs = re.sub("\t", "", lines[i]).strip()
        no_returns = re.sub("\r", "", no_tabs).strip()
        no_newlines = re.sub("\n", " ", no_returns).strip()
        no_extra_spaces = re.sub("\s\s+" , "", no_newlines).strip()
        output = " ".join([output, no_extra_spaces])

    if al_log:
        outputList=re.split(r'.(?=[0-9][0-9][0-9][0-9]\.[0-9][0-9]\.[0-9][0-9] [0-9][0-9]:[0-9][0-9]:[0-9][0-9],[0-9]{1,3})', output)
    elif a7_log:
        outputList=re.split(r'.(?=[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9] [0-9][0-9]:[0-9][0-9]:[0-9][0-9],[0-9]{1,3})', output)
    else:
        print(warnStr, "condense_lines(): Error - Couldn't detect log type (adl or a7service).")
        return
    if debug:
        pass
        #print outputList
    return outputList