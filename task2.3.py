# Build a dictionary of student names and marks, then calculate the average. 

students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 96,
    "Eve": 88
}

total_marks = sum(students.values())
average = total_marks / len(students)

print(f"Average marks of students: {average}")