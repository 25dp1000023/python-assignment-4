file = open('output.txt','w')
text = file.write(input("Enter the text to write the file: ")+"\n")
print("Data successfully written to output.txt.")
file.close()

file = open('output.txt','a')
appending_text = file.write(input("Enter additional data to append: ")+"\n")
print("Data successfully appended.")
file.close()

file = open('output.txt','r')
reading_file = file.read()
print("Final content of output.txt: \n{}".format(reading_file))
file.close()