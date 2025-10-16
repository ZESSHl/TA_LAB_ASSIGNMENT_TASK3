class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class teacher(person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def display_info(self):
        print(f"Teacher: {self.name}, Age: {self.age}")

class student(person):
    def __init__(self, name, age , student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        print(f"Student: {self.name}, Age: {self.age}, ID: {self.student_id}")


class school: 
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, person):
        self.members.append(person)
        print(f"Added {person.name} to {self.name}")

    def show_members(self):
        print(f"\nMembers of {self.name}:")
        for member in self.members:
            member.display_info()


# 1. Inheritance, Student and Teacher can use the same attribute as Person
# 2. Composition, The School has person inside
# 3. making a new class "club" similar to School. Refer to line 45

class Club:
    def __init__(self, name):
        self.name = name
        self.club_members = []

    def add_club_members(self, person):
        self.club_members.append(person)

    def show_club_members(self):
        print(f"\nMembers of {self.name}:")
        for club_member in self.club_members:
            club_member.display_info()

if __name__ == "__main__":
    school = school("BINUS")

    teacher1 = teacher("Daina", 30)
    student1 = student("Maito", 20, "B12345")
    student2 = student("Baum", 22, "B67890")

    school.add_member(teacher1)
    school.add_member(student1)
    school.add_member(student2)

    school.show_members()
    print(f"\n---Club Members---")
    club = Club("CS")

    club.add_club_members(teacher1)
    club.add_club_members(student1)
    club.add_club_members(student2)
    club.show_club_members()
    