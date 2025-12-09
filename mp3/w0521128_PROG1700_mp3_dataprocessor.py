
def read_file(filename):
    """Reads a CSV file and returns a list of lines."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"ERROR: File not found -> {filename}")
        return []



def parse_grades(lines):
    """
    Convert CSV lines into a dictionary:  { "Name": grade }
    Expects first line to be a header.
    """
    grades = {}

    # Using a while-loop because assignment requires one
    index = 1  # skip header line
    while index < len(lines):
        line = lines[index].strip()

        if line != "":
            name, grade = line.split(",")
            grades[name] = int(grade)

        index += 1

    return grades



def process_data(grades_dict):
    """
    Computes:
      - total
      - average
      - highest/lowest
      - passing list
      - failing list
    Returns a dictionary summary.
    """

    total = 0
    highest = None
    lowest = None
    passing = []
    failing = []

    for name, grade in grades_dict.items():

        total += grade

        if highest is None or grade > highest:
            highest = grade

        if lowest is None or grade < lowest:
            lowest = grade

        if grade < 50:
            failing.append(name)
        else:
            passing.append(name)

    average = total / len(grades_dict)

    summary = {
        "total": total,
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "passing": passing,
        "failing": failing
    }

    return summary



def write_report(filename, grades, summary):
    """Writes final summary report to a text file."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("GRADE REPORT\n")
            f.write("----------------------------\n")

            for name, grade in grades.items():
                f.write(f"{name}: {grade}\n")

            f.write("\nSUMMARY\n")
            f.write("----------------------------\n")
            f.write(f"Average Grade: {summary['average']:.2f}\n")
            f.write(f"Highest Grade: {summary['highest']}\n")
            f.write(f"Lowest Grade: {summary['lowest']}\n")
            f.write(f"Passing Students: {summary['passing']}\n")
            f.write(f"Failing Students: {summary['failing']}\n")

    except Exception as e:
        print(f"ERROR writing file: {filename} -> {e}")



def main():
    lines = read_file("grades.csv")

    if not lines:
        print("Program ended (missing grades.csv)")
        return

    grades = parse_grades(lines)
    summary = process_data(grades)
    write_report("grades_summary.txt", grades, summary)

    print("Report created: grades_summary.txt")



if __name__ == "__main__":
    main()


# ---------------------------------------------------------
# 6) Reflection (REQUIRED IN ASSIGNMENT)
# ---------------------------------------------------------
# Reflection:
# 1) Collections used:
#    I used a dictionary to store student:grade pairs because 
#    it is fast for lookup and simple for looping through each record.
#
# 2) Hardest bug fixed:
#    The highest/lowest grade logic originally used 100 and 0 as starting
#    values, which produced wrong results. Changing to None fixed it.
#
# 3) Why file saving is useful:
#    Saving a report allows the data to be used later, shared, or printed. 
#    The user does not need to re-run the program every time.
#
# 4) Feature to add:
#    I would add automatic letter-grade conversion and charts showing 
#    grade distribution.
