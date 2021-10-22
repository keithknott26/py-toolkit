from student import Student
from teacher import Teacher

s = Student('Tom', 'McKoliz', 'A100')
t = Teacher('Maria', 'Giovanetti', 'Math')
print(f'Student name: {s.fullname()}')
print(s.initials())
print(f'Badge number is {s.badge()}')
print("Teacher: {}".format(t.fullname()))
print(t.initials())
