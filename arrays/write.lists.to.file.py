def write_list_to_file(filename, lines_list):
    with open(filename, 'a') as filehandle:
        filehandle.writelines("%s\n" % line for line in lines_list)
    return