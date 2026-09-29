class Phone_book:
    Phone_directory=[]

    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        Phone_book.Phone_directory.append(self)

    def show(self):
        return print(f"Name:{self.name},Contact Number:{self.phone}")

    @classmethod
    def show_all(cls):
        if len(cls.Phone_directory)==0:
            print("Empty")
        else:
            for i in cls.Phone_directory:
                i.show()


c1=Phone_book("John",98472646264)
c2=Phone_book("Mark",8267462542)

Phone_book.show_all()

