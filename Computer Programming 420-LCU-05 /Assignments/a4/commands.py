"""
Gordon Ng 2031408
420-LCU Computer Programming , Section 2
Wednesday, November 24
R. Vincent , instructor
Assignment 4, exercise 2 and 3
"""
def dataEntry(students):
    '''
    students (dict): a dictionary containing inputted records of students, student number and their grades

    Logic for option 1, determines if the record will be accepted based on its length, composition and if its already in the dictionary
    '''
    while True:
        errorCheck = 0  # Determines if the inputed record is valid

        recordInput = ((input('Enter student record (separate fields by commas) or done:')).replace(" ", "")).split(
            ",")  # Turns input into list by removing spaces and splitting at the commas
        if recordInput[0] == "done":
            break
        elif len(recordInput) != 8:  # Checks the length of the resulant list of the input
            print("Record incomplete.  Record rejected.")
        elif not recordInput[0].isalpha():  # Checks if the name is alphabetical
            print("Record invalid.  Record rejected.")
        else:
            for value in range(1, len(recordInput)):
                if not recordInput[value].isdigit():  # Checks if the student ID and grades are digits
                    errorCheck += 1
                    print("Record invalid.  Record rejected.")
                    break
                else:  # Turns digit string to integer
                    recordInput[value] = int(recordInput[value])
            for record in students.keys():
                if recordInput[1] == record:  # Checks for duplicate ID numbers
                    errorCheck += 1
                    print("Duplicate ID number.  Record rejected.")
                    break
            if errorCheck == 0:
                students[recordInput[1]] = recordInput[0], recordInput[1], recordInput[2], recordInput[3], recordInput[4], recordInput[
                    5], recordInput[6], recordInput[7]  # Quick and dirty way to add a student input as an item
                print("Record accepted.")

def average(students):
    '''
    students (dict): a dictionary containing inputted records of students, student number and their grades

    Returns and calculates the rounded class average
    '''
    classAverage = []
    for student in students:  # Gets value from key and turns it into a list to add them up for the average
        tempList = list(students[student])
        classAverage.append(sum(tempList[2:]))  #Adds up the class grade
    return round(sum(classAverage) / len(students))

def dataDisplay(studentGrade, average):
    '''
    studentGrade (int): An integer of a select students overall grade
    average (int): An integer representing the class average

    Compares a students grade with the class average and determines the difference

    Returns a friendly display of the difference between the grade and the class average
    '''
    if studentGrade > average:
        x = studentGrade - average  #difference in grade
        return "{} above class average.".format(x)
    elif studentGrade < average:
        y = average - studentGrade #difference in grade
        return "{} below class average.".format(y)
    else:
        return "at class average. There is a difference of 0 points."

def letterGrade(studentGrade):
    '''
    studentGrade (int): An integer of a select students overall grade

    Compares a students grade and determines their letter grade

    Returns a string letter grade
    '''
    if studentGrade > 87:
        letterGrade = 'A'
    elif studentGrade >= 75:
        letterGrade = 'B'
    elif studentGrade >= 65:
        letterGrade = 'C'
    else:
        letterGrade = 'F'

    return letterGrade

def studentGrade(students, studentID):
    '''
    students (dict): a dictionary containing inputted records of students, student number and their grades
    studentID (int): an integer representing a student's number

    Determines a students grade from their student number

    Returns a students grade
    '''
    for value in students.keys():
        if studentID == value:
            tempList = list(students[value])
            studentGrade = sum(tempList[2:8])
    return studentGrade

def studentName(students, studentID):
    '''
    students (dict): a dictionary containing inputted records of students, student number and their grades
    studentID (int): an integer representing a student's number

    Determines a students name from their student number

    Returns a students name
    '''
    for value in students.keys():
        if studentID == value:
            tempList = list(students[value])
            return tempList[0]


