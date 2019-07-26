from methos import *
import os
import pickle
def load_book():   #func to load book detail in a list from book.pkl file
    curr_book=[]
    if(os.path.isfile("BookInfo.pkl")):
        with open("BookInfo.pkl",'rb') as f:
            while(True):
                try:
                    curr_book=(pickle.load(f))
                except EOFError:
                    break
            f.close()
        return curr_book
    else:
        return False
def load_Student():   #func to load student data in a list from student.pkl file
    curr_student=[]
    if(os.path.isfile("StudentInfo.pkl")):
        with open("StudentInfo.pkl",'rb') as f:
            while(True):
                try:
                    curr_student=(pickle.load(f))
                except EOFError:
                    break
            f.close()
        return curr_student
    else:
        return False
def load_Faculty():     #func to load faculty data in a list from faculty.pkl file
    curr_Faculty=[]
    if(os.path.isfile("FacultyInfo.pkl")):
        with open("FacultyInfo.pkl",'rb') as f:
            while(True):
                try:
                    curr_Faculty=(pickle.load(f))
                except EOFError:
                    break
            f.close()
        return curr_Faculty
def load_Issue():    
    curr_issue=[]
    with open("StudentInfo.pkl",'rb') as f:
        while(True):
            try:
                curr_issue.append(pickle.load(f))
            except EOFError:
                break
        f.close()
        return curr_issue
    
    
    
       