def check_file_exists(filename):
    try:
        open(filename)   # will be a permission error
        return True
    except IOError as e:
        return False
