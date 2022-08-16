def intro():
    print("The grade based on the percentage")
    print("---------------------------------")
    print("""A+ => 90-100%
A  => 85-89%
B+ => 80-84%
B  => 75-79%
C+ => 70-74%
C  => 65-69%
D+ => 60-64%
D  => 50-59%
F  => Lower than 50%""")
    print("---------------------------------")
    gradesList = []
    subjList = ["Math-2", "Logic Design", "Structured Programming", "Probability and Statistics", "Managment", "Critical Thinking"]
    GPA1 = float(input("Enter the GPA of the first term: "))
    gradesAppend(subjList, gradesList, GPA1)

def gradesAppend(subjList, gradesList, GPA1):  
    for i, subj in enumerate(subjList):
        if i == 0 or i == 1 or i == 2 or i == 3:
            hours = 3
        elif i == 4 or i == 5:
            hours = 2

        grade = input(f"Enter your grade in {subj}: ")
        grade = grade.capitalize()

        if grade == "A+":
            gradesList.append(4*hours)
        elif grade == "A":
            gradesList.append(3.7*hours)
        elif grade == "B+":
            gradesList.append(3.3*hours)
        elif grade == "B":
            gradesList.append(3*hours)
        elif grade == "C+":
            gradesList.append(2.7*hours)
        elif grade == "C":
            gradesList.append(2.4*hours)
        elif grade == "D+":
            gradesList.append(2.2*hours)
        elif grade == "D":
            gradesList.append(2*hours)
        elif grade == "F":
            gradesList.append(0)
        else:
            print("Invalid input")
            break

        print("---------------")
    GPACounter(subjList, gradesList, GPA1)

def GPACounter(subjList, gradesList, GPA1):
    sum = 0
    if len(gradesList) < 6:
        gradesList = []
        gradesAppend(subjList, gradesList)
    else:
        for x in gradesList:
            sum += x
        print(f"Your GPA for second term is: {sum/16}")
        print(f"The GPA of the whole year is: {(GPA1+sum/16)/2}")

intro()