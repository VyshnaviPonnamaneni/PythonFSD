class Student:
    subjectname = "Maths"  # Correctly define a class attribute

    def __init__(self, age, rollno, result):
        self.age = age
        self.rollno = rollno
        self.result = result

    def results(self):
        return f"{self.result} is the result of the student"

    @classmethod
    def sub_name(cls, new_sub):
        cls.subjectname = new_sub

# Create an instance of Student
cal = Student(5, 2, 98)

# Accessing the class attribute subjectname
print(cal.subjectname)

# Call the results method
print(cal.results())

# Accessing the instance attributes
print(cal.age)
print(cal.rollno)

# Changing the subject name using the class method
cal.sub_name("Science")
print(cal.subjectname)  # Now it should print "Science"

