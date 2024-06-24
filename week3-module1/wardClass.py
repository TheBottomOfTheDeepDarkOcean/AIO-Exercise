from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob

    @abstractmethod
    def describe(self):
        pass

    def get_yob(self):
        return self._yob

class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        print(f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}")

class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self._specialist = specialist

    def describe(self):
        print(f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}")

class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self._subject = subject

    def describe(self):
        print(f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}")

class Ward:
    def __init__(self, name):
        self._name = name
        self._list_people = list()
    
    def add_person(self, person: Person):
        self._list_people.append(person)

    def describe(self):
        print(f'Name: {self._name}')
        for p in self._list_people:
            p.describe()

    def count_doctor(self):
        counter = 0
        for p in self._list_people:
            if isinstance(p, Doctor):
                counter += 1
        return counter
    
    def sort_yob(self):
        return self._list_people.sort(key = lambda x: x.get_yob())
    
    def compute_average(self):
        counter = 0
        total = 0
        for p in self._list_people:
            if isinstance(p, Teacher):
                counter += 1
                total += p.get_yob()
        return total / counter



if __name__ == "__main__":
    student1 = Student('Thai', 2010, 10)
    doctor1 = Doctor('Duyen', 2003, 5)
    teacher1 = Teacher('Duyen', 2003, 5)
    teacher2 = Teacher('Thai', 2010, 10)

    ward1 = Ward('Ward1')
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    

    ward1.sort_yob()
    ward1.describe()
    print(ward1.compute_average())