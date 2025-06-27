
import Student,pickle

with open('Student.data','rb') as f:
    for i in range (3):
        s = pickle.load(f)
        s.display()
        