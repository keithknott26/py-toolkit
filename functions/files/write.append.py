  if __name__ == '__main__':

    filename = 'myfile.txt'
    with open(filename, 'a') as f:
        f.writelines('this is my file\n') #appending
        f.writelines(' this is another line in my file\n')
        f.writelines('this is next line\n')
