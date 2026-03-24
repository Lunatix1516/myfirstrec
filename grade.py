def calculate_grade(marks):
    average = sum(marks) / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    return average, grade




for i in range(2):  
    name = input("\nStudent name: ")

    marks = []
    print("Enter marks (type 'done' to stop):")

    while True:
        m = input("> ")
        if m == "done":
            break
        marks.append(int(m))

    avg, grade = calculate_grade(marks)
    print(f"{name} -> Average: {avg:.1f}, Grade: {grade}")
