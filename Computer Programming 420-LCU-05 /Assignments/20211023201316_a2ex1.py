"""
Gordon Ng
420-LCU Computer Programming , Section 2
Tuesday , October 26
R. Vincent , instructor 
Assignment 2, Exercise 1
"""
students = [] #List containing tuples of student records

print('Welcome to the Teacher’s Simple Class Calculator. Here’s the list of options:\n  1- Enter student records (Name, ID, and 6 marks separated by commas)\n  2- Display the class average.\n  3- Display the information for a given student\n  4- List the entire class by name and ID.\n  X- Exit')

while True:
  option = input('Select an option by entering its number or X to exit: ')
 
  if option == '1': #Menu option to input student records
    while True:
      errorCheck = 0  #Determines if the inputed record is valid
      studentGrade = 0  #Temporary storage for the inputed grade before it is put into a list

      recordInput = ((input('Enter student record (separate fields by commas) or done:')).replace(" ", "")).split(",")  #Turns input into list by removing spaces and splitting at the commas
      if recordInput[0] == "done":
        break
      elif len(recordInput) != 8: #Checks the length of the resulant list of the input
        print ("Record incomplete.  Record rejected.")     
      elif not recordInput[0].isalpha():  #Checks if the name is alphabetical
        print ("Record invalid.  Record rejected.")
      else:
        for value in range(1, len(recordInput)): 
          if not recordInput[value].isdigit():  #Checks if the student ID and grades are digits
            errorCheck += 1
            print ("Record invalid.  Record rejected.")
            break 
          else: #Turns digit string to integer
            recordInput[value] = int(recordInput[value])
        for record in students:
          if recordInput[1] in record:  #Checks for duplicate ID numbers
            errorCheck += 1
            print ("Duplicate ID number.  Record rejected.")
            break 
        if errorCheck == 0:
          students.append(tuple(recordInput)) #Adds a tuple of the input to the student list
          print ("Record accepted.")  

  elif option == '2': #Menu option to calculate class average
    if len(students) > 0:
      classAverage = []
      for student in students:
        classAverage.append(sum(student[2:8]))
      print ("Class Average is:" , round(sum(classAverage)/len(students)))   
    else:
      print ("No data entered yet.") 

  elif option == '3': #Menu option to search students and their grades from their ID
    if len(students) > 0:
      studentID = input("Enter the ID of the student:")
      if studentID.isdigit():
        studentID = int(studentID)
        for value in students:
          if studentID == value[1]: 
            studentGrade = sum(value[2:8])
            if studentGrade > 87: #Determines the letter grade
              letterGrade = 'A'        
            elif studentGrade >= 75:
              letterGrade = 'B'        
            elif studentGrade >= 65:
              letterGrade = 'C'        
            else:
              letterGrade = 'F'
            print ("Information for", value[0], value[1], "total grade", studentGrade , "letter grade", letterGrade) #Prints out the name, student id, grade, and letter grade
            break
          elif value == students[-1]:
            print ("Invalid, no ID found.")
            break
      else:
        print ("Invalid ID format.")
    else:
      print ("No data entered yet.")

  elif option == '4': #Menu option to print out alphabetically sorted class list with student ID
    classList = []  #Temporary list to store student names
    if len(students) > 0:
      for value in students: #Sort names + student ID
        tempSort = [] #List that is sorted
        tempSort.append(value[0].capitalize()) #Always capitalizes names to avoid sorting problems
        tempSort.append(value[1])
        classList.append(tempSort)
      classList.sort()
      for name in classList: #Matches the sorted name to its student ID then prints it out
        print (name[0], name[1])
    else:
      print ("No data entered yet.")

  elif option == 'x' or option == "X": #Quits the program
    print ('Quitting!')
    break

  else:
    print ('Invalid option! Please choose a number of X to quit.')