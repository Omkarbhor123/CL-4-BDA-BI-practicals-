from collections import defaultdict

# Sample student score data: (Student Name, Score)
students_scores = [("Yash", 85), ("Ritesh", 76), ("Omkar", 92), ("Pratik", 60), ("Harsh", 45)]

# Step 1: Map Function - Assign Grades Based on Score
def assign_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

mapped_data = [(name, assign_grade(score)) for name, score in students_scores]

# Step 2: Reduce Function - Group Students by Grade
grades_grouped = defaultdict(list)
for name, grade in mapped_data:
    grades_grouped[grade].append(name)

# Step 3: Print Final Grade Distribution
for grade, students in grades_grouped.items():
    print(f"Grade {grade}: {', '.join(students)}")
