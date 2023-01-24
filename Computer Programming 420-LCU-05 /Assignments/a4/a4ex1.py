"""
Gordon Ng 2031408
420-LCU Computer Programming , Section 2
Wednesday, November 24
R. Vincent , instructor 
Assignment 4, exercise 1 and 4
"""
import commands

students = {}  # Dictionary of student records

print('Welcome to the Teacher’s Simple Class Calculator. Here’s the list of options:\n  1- Enter student records (Name, ID, and 6 marks separated by commas)\n  2- Display the class average.\n  3- Display the information for a given student\n  4- List the entire class by name and ID.\n  X- Exit')

while True:
    option = input('Select an option by entering its number or X to exit: ')

    if option == '1':  # Menu option to input student records
        commands.dataEntry(students)

    elif option == '2':  # Menu option to calculate class average
        if len(students) > 0:
            print("Class Average is:", commands.average(students))
        else:
            print("No data entered yet.")

    elif option == '3':  # Menu option to search students and their grades from their ID
        if len(students) > 0:
            studentID = input("Enter the ID of the student:")
            if studentID.isdigit():
                studentID = int(studentID)
                if studentID not in students:
                    print("Invalid, no ID found.")
                else:
                    studentGrade = commands.studentGrade(students, studentID)       #Functions from command module defined as easier to read variables
                    studentName = commands.studentName(students, studentID)
                    letterGrade = commands.letterGrade(studentGrade)
                    print("Information for", studentName, studentID, "total grade", studentGrade, "letter grade", letterGrade)  # Prints out the name, student id, grade, and letter grade
                    print("Grade is", commands.dataDisplay(studentGrade, commands.average(students))) #Prints out how much the student is above or below class average
            else:
                print("Invalid ID format.")
        else:
            print("No data entered yet.")

    elif option == '4':  # Menu option to print out alphabetically sorted class list with student ID
        classList = []  # Temporary list to store student names
        if len(students) > 0:
            for value in students:  # Sort names + student ID
                tempSort = []  # List that is sorted
                tempList = list(students[value])
                tempSort.append(tempList[0].capitalize())  # Always capitalizes names to avoid sorting problems
                tempSort.append(value)
                classList.append(tempSort)
            classList.sort()
            for name in classList:  # Matches the sorted name to its student ID then prints it out
                studentID = name[1]
                studentGrade = commands.studentGrade(students, studentID) #Functions from command module defined as easier to read variables
                studentName = commands.studentName(students, studentID)
                letterGrade = commands.letterGrade(studentGrade)
                print("{:10.10s} {:3d} {:3d} {}".format(studentName,studentID,studentGrade,letterGrade)) #Printing formatted class list along with grades
        else:
            print("No data entered yet.")

    elif option == 'x' or option == "X":  # Quits the program
        print('Quitting!')
        break

    else:
        print('Invalid option! Please choose a number or X to quit.')