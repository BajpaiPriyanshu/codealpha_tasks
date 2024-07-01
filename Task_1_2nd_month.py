class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(grade)

    def calculate_average(self):
        total_sum = 0
        count = 0
        for grades in self.grades.values():
            total_sum += sum(grades)
            count += len(grades)
        return total_sum / count if count != 0 else 0

    def __str__(self):
        return f"Student: {self.name}, Average Grade: {self.calculate_average():.2f}"

def main():
    students = {}
    while True:
        action = input("Enter 'add' to add a grade, 'view' to view student averages, or 'exit' to quit: ").lower()
        if action == 'exit':
            break
        elif action == 'add':
            name = input("Enter the student's name: ")
            subject = input("Enter the subject: ")
            grade = float(input("Enter the grade: "))
            if name not in students:
                students[name] = Student(name)
            students[name].add_grade(subject, grade)
        elif action == 'view':
            for student in students.values():
                print(student)
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()