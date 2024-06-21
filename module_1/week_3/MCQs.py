import torch
import torch.nn as nn
from softmax_module import Softmax, SoftmaxStable
from ward import Student, Teacher, Ward, Doctor
from stack import Stack
from queue import Queue


# Q1
data = torch.Tensor([1, 2, 3])
softmax_function = nn.Softmax(dim=0)
output = softmax_function(data)
assert torch.isclose(round(output[0].item(), 2), 0.09, rtol=1e-09, atol=1e-09)
print(f"Q1 result: {output}")

# Q2
data = torch.Tensor([5, 2, 4])
my_softmax = Softmax()
output = my_softmax(data)
assert torch.isclose(round(output[-1].item(), 2), 0.26, rtol=1e-09, atol=1e-09)
print(f"Q2 result: {output}")

# Q3
data = torch.Tensor([1, 2, 30000000])
my_softmax = Softmax()
output = my_softmax(data)
assert torch.isclose(round(output[0].item(), 2), 0.0, rtol=1e-09, atol=1e-09)
print(f"Q3 result: {output}")

# Q4
data = torch.Tensor([1, 2, 3])
softmax_stable = SoftmaxStable()
output = softmax_stable(data)
assert torch.isclose(round(output[-1].item(), 2), 0.67, rtol=1e-09, atol=1e-09)
print(f"Q4 result: {output}")

# Q5
student1 = Student(name="studentZ2023", yob=2011, grade="6")
assert student1.yob == 2011
print(f"Q5 result: {student1.describe()}")

# Q6
teacher1 = Teacher(name="teacherZ2023", yob=1991, subject="History")
assert teacher1.yob == 1991
print(f"Q6 result: {teacher1.describe()}")

# Q7
doctor1 = Doctor(name="doctorZ2023", yob=1981, specialist="Endocrinologist")
assert doctor1.yob == 1981
print(f"Q7 result: {doctor1.describe()}")

# Q8
student1 = Student(name="studentA", yob=2010, grade="7")
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
assert ward1.count_doctor() == 2
print(f"Q8 result: {ward1.count_doctor()}")

# Q9
stack1 = Stack(capacity=5)
stack1.push(1)
assert stack1.is_full() == False
stack1.push(2)
print(f"Q9 result: {stack1.is_full()}")

# Q10
stack1 = Stack(capacity=5)
stack1.push(1)
assert stack1.is_full() == False
stack1.push(2)
print(f"Q10 result: {stack1.top()}")

# Q11
queue1 = Queue(capacity=5)
queue1.enqueue(1)
assert queue1.is_full() == False
queue1.enqueue(2)
print(f"Q11 result: {queue1.is_full()}")

# Q12
queue1 = Queue(capacity=5)
queue1.enqueue(1)
assert queue1.is_full() == False
queue1.enqueue(2)
print(f"Q12 result: {queue1.front()}")