#                                           ***** Advanced Python *****

#  *** Files ***
'''
Files:- A file is a space or location in computer numeric used to store data perminantly.There are 3 modes to open a tent file in python.

        1. Read mode.
        2. Write mode.
        3. append mode.

1.)Read mode:-
            This mode is used to read content from tent. The file pointer always points at the begining of the file.
            The file should be sxist before open mode read mode.

        Ex:- fp=open("D:\\abc.txt","r")

2.)Write mode:-
               >> This mode is used to write content to a file. the cursor always points at the begining of the file.
               >> If file Exists,We will write the content into the file.
               >> If file doesnot exist,it will creates new file with the given name and the write content into the file

        fp=open("D:\\abc.txt","w")

3.) Append mode:- This mode is used to write content to a file.The file pointer always points at end of the file content.
                  If File exist,it will write the content into the file.If file doenot exist.
                  it will creates new file with the given name and write the content into the file.

        Ex:-open("D:\\abc.txt","a")

'''

fp=open("D:\\siva.txt","w")
fp.write("welcome to siva,how are you?")
fp.close
