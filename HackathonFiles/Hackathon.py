import time
import matplotlib.pyplot as plt
import Sorting
import csv
import random
import numpy as np


class Hackathon():
    def __init__(self):
        self.students = []
        self.prepopulate()
        #for s in self.students:
            #print(s)
        

    def prepopulate(self):
        field_names = ['UID', 'LastName', 'FirstName']
        with open('HackathonFiles\cs4222_students_list.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file, fieldnames=field_names)
            for row in csv_reader:
                modules = {#Trying to add random scores for each student to enable us calculate grade
                    'CS4221': random.randint(0, 100),
                    'CS4222': random.randint(0, 100),
                    'CS4141': random.randint(0, 100)
                }
                grade =self.addGrade(modules)
                row['Modules'] = modules # Adding the modules dictionary to the student info
                row['Grade'] = grade
                self.students.append(row)

    def addGrade(self,modules):
        finalscore = 0
        count = 0
        for module, score in modules.items():
            finalscore+= int(score)
            count+=1
        
        finalscore = finalscore/count
        grade = ''
        if(finalscore< 30):
            grade ="F"
        elif (finalscore < 40):
            grade = "D"
        elif (finalscore<55):
            grade = "C"
        elif (finalscore <70):
            grade = "B"
        elif(finalscore <=100):
            grade ="A"
        else:
            grade = "Invalid"
        
        return grade
    
    def print_sorted_students(self):
        students = []
        for s in self.students:
            students.append(s)
        start = time.time()
        Sorting.heap_sort(students,key= lambda x: x['LastName'])
        end = time.time()
        timeTaken1 = start - end

        for s in students:
            print(s)


    

    def Sort_students(self):
        students = []
        for s in self.students:
            students.append(s)
        start = time.time()
        Sorting.heap_sort(students,key= lambda x: x['LastName'])
        end = time.time()
        timeTaken1 = end-start
        return timeTaken1


    def print_searchTop5(self):
        start = time.time()
        topStudents = {'CS4221': [], 'CS4222': [], 'CS41411': []}  # create a list of students in each module
        for module, _ in topStudents.items(): 
            students = [s for s in self.students]  # for loop using list comprehension
            Sorting.heap_sort(students, key=lambda x: x.get(module, 0))  #getting module's scores
            topStudents[module] = students[-5:][::-1] # Get the top 5 students for the current module and reverse the list
        end = time.time()
        timeTaken2 = end - start
        for module, Students in topStudents.items():
            print(f'{module}:\n')
            for x in Students:
                print(f'{x}\n')
    
    def Search_Top5student(self):#Used to get Time Taken
        start = time.time()
        topStudents = {'CS4221': [], 'CS4222': [], 'CS41411': []} 
        for module, _ in topStudents.items(): 
            students = [s for s in self.students]
            Sorting.heap_sort(students, key=lambda x: x.get(module, 0))
            topStudents[module] = students[-5:][::-1]
        end = time.time()
        timeTaken2 = end - start
        return timeTaken2
    
    def PlotTime_Complexity(self,t1,t2):
        x = ['Sort Time', 'Search time']
        y =[t1,t2]
        print(f'Time taken: sort ={t1} search ={t2}')

        plt.bar(x,y,color='c',width=0.3)
        plt.xlabel('Algorithms')
        plt.ylabel('Time Taken')
        plt.title('Time taking for each sorting algorithm')
        plt.show()

    def plot_max_distribution(self):
        # Initialize dictionary to store module grades
        module_grades = {'CS4221': [], 'CS4222': [], 'CS4141': []}

        # Extract grades for each module from the students
        for student in self.students:
            for module, grade in student['Modules'].items():
                if module in module_grades:
                    module_grades[module].append(grade)
        print(module_grades)
        print(self.students)
        # Initialize lists to store grades for each category (A, B, C, D, F) for each module
        grade_categories = {module: {'A': [], 'B': [], 'C': []} for module in module_grades}

        # Populate grade categories
        for module, grades in module_grades.items():
            for grade in grades:
                if grade < 41:
                    grade_categories[module]['C'].append(grade)
                elif grade < 81:
                    grade_categories[module]['B'].append(grade)
                elif grade <= 100:
                    grade_categories[module]['A'].append(grade)
        print(grade_categories)
        
        values1 = []
        values2 = []
        values3 = []
        for module, grades in grade_categories.items():
            count_A = len(grades['A'])
            count_B = len(grades['B'])
            count_C = len(grades['C'])
            values1.append(count_A)
            values2.append(count_B)
            values3.append(count_C)

        print(values1)
        print(values2)
        print(values3)



        # Plotting
        bar_width = 0.25
        categories = ['CS4221','CS4222','CS4141']

        x1 = range(len(categories))
        x2 = [x + bar_width for x in x1]
        x3 = [x + bar_width for x in x2]

        # Plotting
        plt.bar(x1, values1, width=bar_width, color='#FBC4FC', label='0-40')
        plt.bar(x2, values2, width=bar_width, color='#DD82EE', label='40-80')
        plt.bar(x3, values3, width=bar_width, color='#9C27B0', label='81-100')

        # Customize labels and title
        plt.xlabel('Grade Categories')
        plt.ylabel('Number of Students')
        plt.title('Distribution of Grades for Each Module')

        # Customize x-axis ticks
        plt.xticks([x + bar_width for x in range(len(categories))], categories)

        # Add legend
        plt.legend()
        leg = plt.legend(loc = 2, ncol = 3, prop = {'size' : 8})#this doesnt need ncols
        leg.get_frame().set_alpha(0.3)# frame transparency

        # Show plot
        plt.show()


# Main program loop
student_system = Hackathon()

while True:
    print("\nWELOME TO UL'S STUDENT SYSTEM")
    print("Enter 1 to Print Sorted students List")
    print("Enter 2 to Search Top 5 students")
    print("Enter 3 to Create marks distribution plot")
    print('Enter 4 to Crete time complexity plot')
    print('Enter 5 to Exit Student System')

    choice = int(input('Enter your choice: '))
    if choice == 1:
        student_system.print_sorted_students()
    elif choice == 2:
        student_system.print_searchTop5()
    elif choice == 3:
        student_system.plot_max_distribution()
    elif choice == 4:
        t1 = student_system.Sort_students()
        t2 = student_system.Search_Top5student()
        student_system.PlotTime_Complexity(t1,t2)
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please enter a valid option.")
        