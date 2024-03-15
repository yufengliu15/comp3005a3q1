import psycopg2

from config import config

connection = None

def getAllStudents():
    crsr = connection.cursor()
    query = "SELECT * FROM students;"
    crsr.execute(query)
    for tuple in crsr.fetchall():
        print (tuple)
    
def addStudent(first_name, last_name, email, enrollment_date):
    crsr = connection.cursor()
    query = "INSERT INTO students (first_name, last_name, email, enrollment_date)\
    VALUES (%s, %s, %s, %s)"
    insert_value = (first_name, last_name, email, enrollment_date)
    
    crsr.execute(query, insert_value)

def updateStudentEmail(student_id, new_email):
    crsr = connection.cursor()
    query = "UPDATE students\
             SET email=%s\
             WHERE student_id=%s"
    insert_value = (new_email, student_id)
    
    crsr.execute(query, insert_value)
    
def deleteStudent(student_id):
    crsr = connection.cursor()
    query = "DELETE FROM students\
             WHERE student_id=%s"
    insert_value = (student_id)
    
    crsr.execute(query, insert_value)


def menu():
    userInput = -1
    while (userInput != 0):
        print("1) getAllStudents() test")
        print("2) addStudent(first_name, last_name, email, enrollment_date) test")
        print("3) updateStudentEmail(student_id, new_email) test")
        print("4) deleteStudent(student_id) test")
        print("0) Exit")
        userInput = int(input())
        
        match userInput:
            case 1:
                getAllStudents()
            case 2:
                print("First Name: ")
                first_name = input()
                print("Last Name: ")
                last_name = input()
                print("Email: ")
                email = input()
                print("Enrollment Date: ")
                enrollment_date = input()
                addStudent(first_name, last_name, email, enrollment_date)
                print("Successfully added in ", first_name, last_name)
            case 3:
                print("Student ID: ")
                student_id = input()
                print("Email: ")
                email = input()
                updateStudentEmail(student_id, email)
                print("Successfully updated ID:", student_id, "'s email to ", email)
            case 4:
                print("Student ID: ")
                student_id = input()
                deleteStudent(student_id)
                print("Successfully delete student ID: ", student_id)
                
                
# =========================== main ================================
try:
    params = config()
    
    connection = psycopg2.connect(**params)
    print("Successfully connected to the database")
    print("=================================")
    connection.autocommit = True
    menu()
except(Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if connection is not None:
        connection.close()
        print("=================================")
        print("Connection terminated.")
