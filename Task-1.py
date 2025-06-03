try:
    file=open('sample.txt','w')
    writing_file=file.write('Reading file content:\nLine 1: This is a sample text file.\nLine 2: It contains multiple lines.')
    file.close()

    file1 = open('sample.txt', 'r')
    reading_file1 = file1.read()
    print(reading_file1)
    file1.close()
except FileNotFoundError:
    print('Error: The file \'sample text\' was not found.')