class Student:
    def __init__(self,name,subject,village,number):
        self.name = name
        self.subject = subject
        self.village = village
        self.number = number

    def good_student(self,country):
        print(country)

    def student(self,mandal):
        print(mandal)

s1 = Student('vamsi','python','bichuvaripalle','8179828084')
s2 = Student('anil','pl/sql','potladhutthi','9951430712')
s3 = Student('naveen','python','matli','8297565729')
print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)
s1.good_student('india')
s2.good_student('india')
s3.good_student('india')
s1.student('kajipeta')
s2.student('erraguntla')
s3.student('veeraballi')

