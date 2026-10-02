
# Student Grade Manager

students = []


def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    try:
        mark = int(input("Enter marks (0-100): "))

        if mark < 0 or mark > 100:
            print("Invalid marks! Enter a number from 0 to 100.")
            return

    except ValueError:
        print("Invalid input! Please enter a whole number.")
        return

    student = {
        "name": name,
        "mark": mark,
        "grade": get_grade(mark)
    }

    students.append(student)
    print(f"Student {name} added successfully!")


def show_results():
    if not students:
        print("No students added yet.")
        return

    print("\n" + "=" * 40)
    print(f"{'Name':<15}{'Mark':<10}{'Grade':<10}")
    print("-" * 40)

    for student in students:
        print(
            f"{student['name']:<15}"
            f"{student['mark']:<10}"
            f"{student['grade']:<10}"
        )

    marks = [student["mark"] for student in students]

    average = sum(marks) / len(marks)

    print("-" * 40)
    print(f"Class average: {average:.1f}")
    print(f"Highest mark: {max(marks)}")
    print(f"Lowest mark: {min(marks)}")
    print("=" * 40)


while True:
    print("\n--- Student Grade Manager ---")
    print("1. Add student")
    print("2. Show results")
    print("3. Quit")

    choice = input("Choose an option (1-3): ").strip()

    if choice == "1":
        add_student()

    elif choice == "2":
        show_results()

    elif choice == "3":
        print("Thank you for using Student Grade Manager!")
        break

    else:
        print("Invalid choice! Please select 1, 2, or 3.")
