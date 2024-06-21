class Ward:
    def __init__(self, name):
        self.name = name
        self.persons = []

    def describe(self):
        print(f"--------------------{self.name}--------------------")
        for i in range(len(self.persons)):
            print(f"No.{i}: {self.persons[i].describe()}")

    def add_person(self, person):
        self.persons.append(person)

    def count_doctor(self):
        doctor_count = 0
        for person in self.persons:
            if person.occupation == "Doctor":
                doctor_count += 1

        return doctor_count

    def sort_age(self):
        def get_yob(person):
            return person.yob

        self.persons.sort(key=get_yob)

    def compute_average(self):
        total_yob = sum([person.yob for person in self.persons])
        return total_yob / len(self.persons)


class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    def describe(self):
        return f"Name: {self.name} - YoB: {self.yob}"


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade
        self.occupation = "Student"

    def describe(self):
        return f"{self.occupation} - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}"


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject
        self.occupation = "Teacher"

    def describe(self):
        return f"{self.occupation} - Name: {self.name} - YoB: {self.yob} - Teaching: {self.subject}"


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist
        self.occupation = "Doctor"

    def describe(self):
        return f"{self.occupation} - Name: {self.name} - YOB: {self.yob} - Specialize in: {self.specialist}"


ward1 = Ward("Ward1")
student1 = Student(name="studentA", yob=2010, grade=7)
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

print(f"\nNumber of doctors: {ward1.count_doctor()}")
ward1.sort_age()
ward1.describe()
print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")
