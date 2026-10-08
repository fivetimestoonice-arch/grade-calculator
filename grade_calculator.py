# import numpy as np will be used for v2/3
# import pandas as pd will be used for v2/3


def student_information():

    while True:
        name = input("Enter your name: ").strip()
        if not name:
            print("Name cannot be empty. Please enter a valid name.")
            continue
        break

    while True:
        try:
            age = int(input("Enter your age: "))
            if age <= 0:
                print("Age must be a positive integer. Please enter a valid age.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for age.")

    return name, age


# V2: RETRIEVE_STUDENT_INFORMATION/STUDENT_SEARCH() - (This function will be used to search your local computer for saved files from the report card generator. It will allow you to retrieve your previous report cards and view them without having to re-enter your information.)


def allocating_percentages_to_subjects():
    all_grades = []
    subjects = []

    while True:
        subject = input("Enter subject name (or type 'done' to finish): ").strip()

        if not subject:
            print("Subject name cannot be empty. Please enter a valid subject.")
            continue

        if subject.lower() == "done":
            break

        choice = input("Enter (p) for percentage or (m) for marks: ").strip().lower()

        if choice == "p":
            while True:
                try:
                    grade = float(input("Enter your percentage: "))
                    if 0 <= grade <= 100:
                        break
                    print(
                        "Percentage must be between 0 and 100. Please enter a valid percentage."
                    )
                except ValueError:
                    print("Invalid input. Please enter a numeric percentage.")

            all_grades.append(grade)
            subjects.append(subject)

        elif choice == "m":
            while True:
                try:
                    earned_marks = float(input("Enter your earned marks: "))
                    total_marks = float(input("Enter total number of marks: "))

                    if total_marks <= 0:
                        print("Total marks must be greater than 0.")
                        continue

                    if earned_marks < 0 or earned_marks > total_marks:
                        print(
                            "Earned marks cannot be negative or greater than total marks. Please enter valid marks."
                        )
                        continue

                    break
                except ValueError:
                    print("Invalid input. Please enter numeric values for marks.")

            grade = (earned_marks / total_marks) * 100
            all_grades.append(grade)
            subjects.append(subject)

        else:
            print("Please enter (p) or (m)")

    return subjects, all_grades


def metric_grading_system(all_grades, threshold):
    Lettergrades = []

    for grade in all_grades:
        if grade >= threshold["A"]:
            Lettergrades.append("A")
        elif grade >= threshold["B"]:
            Lettergrades.append("B")
        elif grade >= threshold["C"]:
            Lettergrades.append("C")
        elif grade >= threshold["D"]:
            Lettergrades.append("D")
        elif grade >= threshold["E"]:
            Lettergrades.append("E")
        else:
            Lettergrades.append("U")

    return Lettergrades


def set_grade_thresholds():

    Default_thresholds = input(
        "Do you want to use default grade thresholds or custom grade thresholds?\nEnter (d) for default or (c) for custom: "
    ).lower()

    if Default_thresholds == "d":
        threshold = {"A": 90, "B": 80, "C": 70, "D": 60, "E": 50, "U": 0}
    else:
        threshold = {}
        grades_order = ["A", "B", "C", "D", "E", "U"]

    while True:
        try:
            for grade in grades_order:
                threshold[grade] = float(
                    input(f"Enter the minimum percentage for grade {grade}: ")
                )

            # Validate that thresholds are in descending order
            if (
                threshold["A"]
                > threshold["B"]
                > threshold["C"]
                > threshold["D"]
                > threshold["E"]
                > threshold["U"]
            ):
                break
            else:
                print(
                    "Thresholds must be in descending order. Please re-enter the values."
                )
        except ValueError:
            print("Invalid input. Please enter numeric values for thresholds.")

    return threshold


# def DATA ANALYSIS():
# This function can be implemented later for analyzing the grades, predicting outcomes, and providing insights.


def display_report_card(name, age, subjects, grades, letter_grades):
    print("\n" + "=" * 60)
    print(f"Report Card for {name} (Age: {age})")
    print("=" * 60)

    for subject, grade, letter in zip(subjects, grades, letter_grades):
        print(f"{subject:<20} {grade:>7.2f}%  {letter}")

    if grades:
        average = sum(grades) / len(grades)
        print("-" * 60)
        print(f"{'Average':<20} {average:>7.2f}%")

    print("=" * 60)


def main():
    name, age = student_information()
    threshold = set_grade_thresholds()
    subjects, all_grades = allocating_percentages_to_subjects()
    letter_grades = metric_grading_system(all_grades, threshold)
    display_report_card(name, age, subjects, all_grades, letter_grades)
    input("Press Enter to exit...")


if __name__ == "__main__":
    main()
