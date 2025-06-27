import Student,pickle

studs = [Student.Student(10,'John','CS'),Student.Student(13,'Chandan','DSAI'),Student.Student(50,'Raj','ECE')]

with open('Student.data', 'wb') as f:
    for s in studs:
        pickle.dump(s,f)

    
