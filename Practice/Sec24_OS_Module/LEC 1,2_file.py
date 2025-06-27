# LECTURE 02:
import os

# print(os.path.exists('C:\\Users\\Arjun\\Python\\Python Online Cource\\Concept Pratice\\Section 24 OS Module\\Child 01\\CPP.jpg'))

# print(os.path.isfile('C:\\Users\\Arjun\\Python\\Python Online Cource\\Concept Pratice\\Section 24 OS Module\\Child 01\\CPP.jpg'))

# print(os.path.isdir('C:\\Users\\Arjun\\Python\\Python Online Cource\\Concept Pratice\\Section 24 OS Module\\Child 01\\CPP.jpg'))   # It is file.

# print(os.path.isdir('C:\\Users\\Arjun\\Python\\Python Online Cource\\Concept Pratice\\Section 24 OS Module\\Child 01'))    # It is directory.


# print(os.path.split('C:\\Users\\Arjun\\Python\\Python Online Cource\\Concept Pratice\\Section 24 OS Module\\Child 01\\CPP.jpg'))    



# print(os.path.join('C:\\Users\\Arjun\\Python\\Python Online Cource\\Concept Pratice\\Section 24 OS Module\\Child 01' , 'CPP.jpg'))    

# print(os.path.basename('C:\\Users\\Arjun\\Python\\Python Online Cource\\Concept Pratice\\Section 24 OS Module\\Child 01\\CPP.jpg'))   

# print(os.path.dirname('C:\\Users\\Arjun\\Python\\Python Online Cource\\Concept Pratice\\Section 24 OS Module\\Child 01\\CPP.jpg'))  


# print(os.path.getmtime('C:\\Users\\Arjun\\Python\\Python Online Cource\\Concept Pratice\\Section 24 OS Module\\Child 01\\CPP.jpg')) 
# import time   
# print(time.ctime(os.path.getmtime('C:\\Users\\Arjun\\Python\\Python Online Cource\\Concept Pratice\\Section 24 OS Module\\Child 01\\CPP.jpg'))) 

# print(os.path.getatime('C:\\Users\\Arjun\\Python\\Python Online Cource\\Concept Pratice\\Section 24 OS Module\\Child 01\\CPP.jpg')) 
# import time  
# print(time.ctime(os.path.getatime('C:\\Users\\Arjun\\Python\\Python Online Cource\\Concept Pratice\\Section 24 OS Module\\Child 01\\CPP.jpg'))) 


# print(os.path.getctime('C:\\Users\\Arjun\\Python\\Python Online Cource\\Concept Pratice\\Section 24 OS Module\\Child 01\\CPP.jpg')) 
# import time  
# print(time.ctime(os.path.getctime('C:\\Users\\Arjun\\Python\\Python Online Cource\\Concept Pratice\\Section 24 OS Module\\Child 01\\CPP.jpg'))) 


# os.chdir('C:\\Users\\Arjun\\Python\\Python Online Cource\\Concept Pratice\\Section 24 OS Module\\Child 01')
# print(os.getcwd())
# # print(os.path.relpath('C:\\Users\\Arjun\\Python\\Python Online Cource\\Concept Pratice\\Section 24 OS Module\\Child 02\\DPU.png'))     # It give relative path Output:  ..\Child 02\DPU.png
# print(os.path.abspath('..\Child 02\DPU.png'))     # It give Absolute path Output:  ..\Child 02\DPU.png



# LECTURE 02: OS MODULE

# print(os.name)   # 'nt' is short for technology used by window 
# print(os.getlogin())   # it tell the window running with whch name.

# print(os.getcwd())     # It show the current directory

# os.chdir('C:\\Users\\Arjun\\Python\\Python Online Cource\\Practice')
# print(os.getcwd())                # Show the change directory:

# print(os.listdir())   # it show the all the file and folder persent in given directory


# print(os.mkdir('C:\\Users\\Arjun\\Python\\Python Online Cource\\Concept Pratice\\Section 24 OS Module\\Child 03'))   # it instant create a folder in whatever u given a path


# print(os.makedirs('C:\\Users\\Arjun\\Python\\Python Online Cource\\Concept Pratice\\Section 24 OS Module\\Gparent01\\Parent\\Child'))   # it instant create a multiple nested folder in whatever u given a path

# print(os.remove('C:\\Users\\Arjun\\Python\\Python Online Cource\\Concept Pratice\\Section 24 OS Module\\Gparent\\Parent\\Child\\CPP.jpg'))     # it can delete single file

# print(os.rmdir('C:\\Users\\Arjun\\Python\\Python Online Cource\\Concept Pratice\\Section 24 OS Module\\Child 03'))    # It can delete a single folder

# print(os.removedirs('C:\\Users\\Arjun\\Python\\Python Online Cource\\Concept Pratice\\Section 24 OS Module\\Gparent01\\Parent\\Child'))   # It can delete multiple nested folder


# print(os.rename('C:\\Users\\Arjun\\Python\\Python Online Cource\\Concept Pratice\\What are module','C:\\Users\\Arjun\\Python\\Python Online Cource\\Concept Pratice\\What Are Module?'))   # It can rename the folder name, We cannot change the name of running folder




































