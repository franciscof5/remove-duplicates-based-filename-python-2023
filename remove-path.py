# Python code to
# demonstrate readlines()
import os
L = ["Geeks\n", "for\n", "Geeks\n"]
 
# writing to file
file2 = open('files-google-numeros', 'w')


# Using readlines()
file1 = open('files-google', 'r')
Lines = file1.readlines()
 
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    #os.path.join(os.path.dirname(os.path.dirname(path)),
                 #)
    print(  os.path.basename(line.strip())[2:8] )
    file2.writelines(os.path.basename(line.strip())[2:8] + "\n" )

file2.close()
