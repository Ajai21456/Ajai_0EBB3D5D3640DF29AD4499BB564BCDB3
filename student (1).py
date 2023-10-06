def sort_students(student_list):
    # Use the sorted function to sort the student_list based on the 'cgpa' attribute in descending order
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Define the Student class
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Test the function with a list of student objects
if __name__ == "__main__":
    # Creating a list of student objects
    students = [
        Student("Alice", "101", 3.9),
        Student("Bob", "102", 3.7),
        Student("Charlie", "103", 3.5),
        Student("David", "104", 3.8)
    ]

    # Sorting the list of students by CGPA
    sorted_students = sort_students(students)

    # Printing the sorted list
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
