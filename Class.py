class SDetail:  # student detail
    def __init__(self,name,year,rollno,dept,today,count,Isbn,dit,lt,Fine):
        self.name=name
        self.year=year
        self.rollno=rollno
        self.dept=dept
        self.today=today
        print(self.today)
        print("hey")
        self.count=count
        self.Isbn=Isbn
        self.dit=dit
        self.lt=lt
        self.Fine=Fine
    def display(self):
        print(f"student name{self.name}")
        print(f"student rollnumber {self.rollno}")
        print(f"student department {self.dept}")
        print(f"student's Fine {self.Fine}")
        print(f"book issued {self.dit}")
        
class FDetail:   #faculty detail
    def __init__(self,name,FacultyId,dept,today,count2,Isbn,dit2,lt2):
        self.name=name
        self.FacultyId=FacultyId
        self.dept=dept
        self.today=today
        self.count2=count2
        self.Isbn=Isbn
        self.dit2=dit2
        self.lt2=lt2
    def display(self):
        print(f"Faculty name{self.name}")
        print(f"faculty ID {self.FacultyId}")
        print(f"faculty department {self.dept}")
        print(f"book issued {self.dit2}")
class BookDetail:    #books detail
    def __init__(self,book_title,book_author,book_publication,book_pub_year,book_isbn,book_no):
        self.book_title=book_title
        self.book_author=book_author
        self.book_publication=book_publication
        self.book_pub_year=book_pub_year
        self.book_isbn=book_isbn
        self.book_no=book_no
    def display(self):
        print(f"book tittle {self.book_title}")
        print(f"book author {self.book_author}")
        print(f"book publication {self.book_publication}")
        print(f"book publication year {self.book_pub_year}")
        print(f"book isbn {self.book_isbn}")
        print(f"book number {self.book_no}")

        