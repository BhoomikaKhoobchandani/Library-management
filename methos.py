from datetime import *
from Class import *   #importing class.py file
from load import *    #importing load.py file 
import pickle   
def AddStudent():     #adding student to the data base
    name=input("ENTER STUDENT'S NAME")
    #l1=[]
    year=int(input("ENTER ADMISSION YEAR"))
    today = datetime.today()
    collegecode="0187"
    datem = datetime(today.year, today.month, 1)
    if(today.year>=year and today.year<=(year+4)):
        dept=input("ENTER Department")
        rollLast=(input("ENTER LAST FOUR DIGIT OF ROLL NUMBER"))
        y=str(year)
        rollno=collegecode+dept+y[2:4]+rollLast
        check,l=SearchStudent(rollno)
        if(check==True):
            print("Already exist")
        elif(check==False and l==False):
            l1=[]
            with open("StudentInfo.pkl",'wb') as f:
                count=0
                Isbn=0
                dit={}
                lt=[]
                Fine=0
                s=SDetail(name,year,rollno,dept,today,count,Isbn,dit,lt,Fine)
                l1.append(s)
                pickle.dump(l1,f)
                print("Information Fed Sucesssfully")
            
        else:
            with open("StudentInfo.pkl",'wb') as f:
                count=0
                Isbn=0
                dit={}
                lt=[]
                Fine=0
                s=SDetail(name,year,rollno,dept,today,count,Isbn,dit,lt,Fine)
                l.append(s)
                pickle.dump(l,f)
                print("Information Fed Sucesssfully")
    else:
        print("SORRY YOU ARE NO LONGER USER")
        
def AddFaculty():      #func to add faculty to the data base 
    name=input("ENTER CANDIDATE'S NAME")
    today = datetime.today()
    FacultyId=input("FacultyId")
    datem = datetime(today.year, today.month, 1)
    dept=input("ENTER Department")
    check,l1=SearchFaculty(FacultyId)
    if(check==True):
        print("Already exist")
    elif(check==False and l1==None):
        with open("FacultyInfo.pkl",'wb') as f:
            count2=0
            Isbn=0
            dit2={}
            l2=[]
            lt2=[]
            fa=FDetail(name,FacultyId,dept,today,count2,Isbn,dit2,lt2)
            l2.append(fa)
            pickle.dump(l2,f)
            f.close()
            print("Information Fed Sucesssfully")
        
    else:
        with open("FacultyInfo.pkl",'wb') as f:
                count2=0
                Isbn=0
                dit2={}
                lt2=[]
                fa=FDetail(name,FacultyId,dept,today,count2,Isbn,dit2,lt2)
                l1.append(fa)
                pickle.dump(l1,f)
                f.close()
                print("Information Fed Sucesssfully")
            
def add_book(): #func to add new book in data base
    c=str()
    l2=load_book()
    re=input("reenterring any book! If yes then PRESS Y space book isbn or else press N")
    while(c!='Y'):
        if(re=='N'):
            book_author = input('Enter the book author: ')
            book_publication = input('Enter the book publication: ')
            book_pub_year =int(input('Enter the year of publication of book: '))
            book_isbn = int(input(('Enter the ISBN code of book: ')))
            book_no=0
            book_title =input('Enter the book title: ')
            book_no=int(input("enter number of copies"))
        else:
            book_title =input('Enter the book title: ')
            book_author = input('Enter the book author: ')
            book_publication = input('Enter the book publication: ')
            book_pub_year =int(input('Enter the year of publication of book: '))
            book_isbn = int(input(('Enter the ISBN code of book: ')))
            book_no+=1
        c=input("Are you done? Y or N")
    if(l2==False):
        l3=[]
        with open("BookInfo.pkl",'wb') as f:
            b=BookDetail(book_title,book_author,book_publication,book_pub_year,book_isbn,book_no)
            l3.append(b)
            pickle.dump(l3,f)
            print("Information Successfully Fed")
        
    else:
         with open("BookInfo.pkl",'wb') as f:
                b=BookDetail(book_title,book_author,book_publication,book_pub_year,book_isbn,book_no)
                l2.append(b)
                pickle.dump(l2,f)
                print("Information Successfully Fed")
def searchBook(M,data):      #func to search particular book in data base
    s=load_book()
    c=0
    d=len(s)
    for i in s:
        if(M=='isbn' and int(data)==i.book_isbn):
            print("book found")
            return(True)
        if(M=='Author' and str(data)==i.book_author):
            print("book found")
            return(True)
        if(M=='Title' and str(data)==i.book_title):
            print("book found")
            return(True)
    return(False)
def SearchStudent(data):       #func to search particular student in data base
    s1=load_Student()
    if(s1):
        for i in s1:
            if(data==i.rollno):
                return(True,s1)
        return(False,s1)
    else:
        return(False,s1)
    
def SearchFaculty(data):       #func to search particular faculty in data base
    s=load_Faculty()
    if(s):
        for i in s:
            if(data==i.FacultyId):
                return(True,s)
        return(False,s)
    else:
        return(False,s)
def AlreadyIssueBook(roll,BIsbn):   #func to check if particular student have already issued mentioned isbn book
    r=load_Student()
    for k in r:
        if(k.rollno==roll and k.Isbn==BIsbn):
            return False
    return True  
def AlreadyIssueBookF(roll,BIsbn):       #func to check if particular faculty have already issued mentioned isbn book
    r=load_Faculty()
    for k in r:
        if(k.FacultyId==roll and k.Isbn==BIsbn):
            return False
    return True  
def StudentData(roll,IS):            #func to mentioned partcular 
    t=load_Student()
    print(t)
    for k in t:
        #k.display()
        if(k.rollno==roll):
            for key,value in k.dit.items():
                if(key==roll):
                    print(key)
                if IS in k.lt:
                    return key
        return False
def FacultyData(roll,IS):
    t=load_Faculty()
    for i in t:
        print(type(i.dit2))
        for key,value in i.dit2.items():
            if(key==roll):
                print(key)
                if IS in i.lt2:
                    return key
        return False
def CalcFine(roll):       #func to calculate fine of particular student
    u=load_Student()
    d1=input("enter month/date/year")
    ReturnDate=datetime.strptime(d1,"%m/%d/%Y")
    for i in u:
        r=abs((i.today)-(ReturnDate))
        #print("you are late by",r)
        return(r)

            
def IssueBook(rollnoG):        #func to issue book to particular student
    c=SearchStudent(rollnoG)   #searching student exist or not
    d=load_Student()           #loading student detail from pickle file
    store=load_book()
    if(c):
        for  i in d:
            if(i.rollno==rollnoG):
                Isbn=int(input("enter book isbn"))
                Find=AlreadyIssueBook(i.rollno,Isbn)
                if(Find):
                    for j in store:
                        if(j.book_isbn==Isbn and j.book_no>0):
                            if(i.count<=2):
                                with open("StudentInfo.pkl",'wb') as f:
                                    with open("BookInfo.pkl",'wb')as f1:
                                        today = datetime.today()
                                        i.count+=1
                                        print(i.count)
                                        i.Isbn=Isbn
                                        i.lt.append(i.Isbn)
                                        i.dit={i.rollno:i.lt}
                                        print(i.lt)
                                        j.book_no-=1
                                        pickle.dump(store,f1)
                                        j.display()
                                        #s1=SIssue(i.rollno,i.count,i.Isbn,today,i.dit,i.lt)
                                        pickle.dump(d,f)
                                        f1.close()
                                        f.close()
                                        print("book issued succesfully")
                                        return True
                            if(i.count>2):
                                print("Student Has Reached Book Limit. Cannot Issue Book.")
                    else:
                        print("Not in Store")
                        return False
                else:
                    print("already Issued")
                    return False
        if(i.count>2):
            print("Student Has Reached Book Limit. Cannot Issue Book.")
    else:
        print("Student not found. Cannot Issue Book")
def IssueBookF(rollnoG):       #func to issue book to particular faculty
    c=SearchFaculty(rollnoG)
    d=load_Faculty()
    store=load_book()
    if(c):
        for  i in d:
            if(i.FacultyId==rollnoG):
                Isbn=int(input("enter book isbn"))
                Find2=AlreadyIssueBookF(i.FacultyId,Isbn)
                if(Find2):
                    for j in store:
                        if(j.book_isbn==Isbn and j.book_no>0):
                            if(i.count2<=2):
                                with open("FacultyInfo.pkl",'wb') as f:
                                     with open("BookInfo.pkl",'wb')as f1:
                                            today = datetime.today()
                                            i.count2+=1
                                            print(i.count2)
                                            i.Isbn=Isbn
                                            i.lt2.append(i.Isbn)
                                            i.dit2={i.FacultyId:i.lt2}
                                            print(i.dit2)
                                            j.book_no-=1
                                            pickle.dump(store,f1)
                                            #s1=SIssue(i.rollno,i.count,i.Isbn,today,i.dit,i.lt)
                                            pickle.dump(d,f)
                                            f1.close()
                                            f.close()
                                            print("book issued succesfully")
                                            return True
                            if(i.count2>2):
                                print("This ID Has Reached Book Limit. Cannot Issue Book.")
                    else:
                        print("Not in Store")
                        return False
                else:
                    print("already Issued")
                    return False
        if(i.count2>2):
            print("This Id Has Reached Book Limit. Cannot Issue Book.")
    else:
        print("ID not found. Cannot Issue Book")
def ReturnBookS(roll):      #func to return book to the library by student
    c=SearchStudent(roll)
    s=load_Student()
    d2=load_book()
    if(c):
        for  i in s:
            if(i.rollno==roll):
                print(i.dit)
                IS=int(input("Enter Isbn Number"))
                temp=StudentData(roll,IS)
                if(temp):
                    i.fine=CalcFine(roll)
                    if(i.Fine):
                        print("you are late by=",(i.Fine))
                    else:
                        print("No Fine")
                    with open("StudentInfo.pkl",'wb') as f:
                         with open("BookInfo.pkl",'wb')as f1:
                                for j in d2:
                                    if(j.book_isbn==IS):
                                        j.book_no+=1
                                        j.display()
                                        pickle.dump(d2,f1)
                                if IS in i.lt:  
                                    i.lt.remove(IS)
                                pickle.dump(s,f)
                                f.close()
                                f1.close()
                else:
                    print("Book with ISBN: {book_isbn} has not been issued to this student")
        
    else:
        print("Student not present in database.Error!")
def ReturnBookF(roll):     #func to return book to library by faculty
    c=SearchFaculty(roll)
    s=load_Faculty()
    d2=load_book()
    if(c):
        for  i in s:
            if(i.FacultyId==roll):
                IS=int(input("Enter Isbn Number"))
                temp=FacultyData(roll,IS)
                if(temp):
                    with open("FacultyInfo.pkl",'wb') as f:
                        with open("BookInfo.pkl",'wb')as f1:
                            for j in d2:
                                if(j.book_isbn==IS):
                                    j.book_no+=1
                                    j.display()
                                    pickle.dump(d2,f1)
                                if IS in i.lt2:
                                    i.lt2.remove(IS)
                                    pickle.dump(s,f)
                                    f.close()
                                f1.close()
                else:
                    print("Book with ISBN: {book_isbn} has not been issued to this student")
        
    else:
        print("Student not present in database.Error!")
def StudentDisplay():   #func to display student data
    ss=load_Student()
    for i in ss:
        i.display()
def FacultyDisplay():     #func to display faculty data
    sf=load_Faculty()
    for i in sf:
        i.display()
def BookDisplay():      #func to display book data
    sb=load_book()
    for i in sb:
        i.display()
        
    
    
    
