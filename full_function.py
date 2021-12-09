from colorama import Fore
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="school"
)

loop = True

def student():
    print(Fore.GREEN + '##########################################################################')
    print(Fore.GREEN + '#WELCOME TO STUDENT LOBBY HERE YOU CAN VIEW ANY STRAND AND THEIR SUBJECTS#')
    print(Fore.GREEN + '##########################################################################')
    comm = input('Input your Grade Level (11 or 12)\nPress [X] to Exit Programm\n:')
    if comm == '11':
        strand = input('Press [S] for STEM\nPress [H] for HUMMS\nPress [A] for ABM\n:')
        if strand == 's' or strand == 'S':
            comm = input('Press [1] to View subjects for 1st Semester\nPress [2] to View subjects for 2nd Semester\n:')
            if comm == '1':
                subj1 = ['21st Century Literature', 'Earth Science', 'General Mathematics', 'Komunikasyon at Pananaliksik', 'Oral Communication', 'Physical Education 1']
                subj2 = ['Empowerment Technologies']
                subj3 = ['General Biology 1', 'Pre - Calculus']
                print(Fore.MAGENTA + 'LIST OF SUBJECTS FOR FIRST SEMESTER')
                print(Fore.RED + 'CORE SUBJECTS')
                for core in subj1:
                    print(Fore.CYAN + core)
                print(Fore.RED + 'APPLIED SUBJECTS')
                for core2 in subj2:
                    print(Fore.CYAN + core2)
                print(Fore.RED + 'SPECIALIZED SUBJECTS')
                for core3 in subj3:
                    print(Fore.CYAN + core3)
                student()
            elif comm == '2':
                subj1 = ['DRRR', 'Pagbasa at Pagsusuri', 'Personal Development', 'PE 2', 'Reading and Writing', 'Statistics and Probability']
                subj2 = ['EASP', 'Practical Research 1']
                subj3 = ['Basic Calculus', 'General Biology 2']
                print(Fore.MAGENTA + 'LIST OF SUBJECTS FOR SECOND SEMESTER')
                print(Fore.RED + 'CORE SUBJECTS')
                for core in subj1:
                    print(Fore.CYAN + core)
                print(Fore.RED + 'APPLIED SUBJECTS')
                for core2 in subj2:
                    print(Fore.CYAN + core2)
                print(Fore.RED + 'SPECIALIZED SUBJECTS')
                for core3 in subj3:
                    print(Fore.CYAN + core3)
                student()
        elif strand == 'h' or strand == 'H':
            comm = input('Press [1] to View subjects for 1st Semester\nPress [2] to View subjects for 2nd Semester\n:')
            if comm == '1':
                subj1 = ['21st Century Literature', 'Earth Science', 'General Mathematics', 'Komunikasyon at Pananaliksik', 'Oral Communication', 'Physical Education 1']
                subj2 = ['Empowerment Technologies']
                subj3 = ['Phillippine Politics and Governance', 'Discipline and Idea in the Social Sciences']
                print(Fore.MAGENTA + 'LIST OF SUBJECTS FOR FIRST SEMESTER')
                print(Fore.RED + 'CORE SUBJECTS')
                for core in subj1:
                    print(Fore.CYAN + core)
                print(Fore.RED + 'APPLIED SUBJECTS')
                for core2 in subj2:
                    print(Fore.CYAN + core2)
                print(Fore.RED + 'SPECIALIZED SUBJECTS')
                for core3 in subj3:
                    print(Fore.CYAN + core3)
                student()
            elif comm == '2':
                subj1 = ['Physical Science', 'Pagbasa at Pagsusuri', 'Personal Development', 'PE 2', 'Reading and Writing', 'Statistics and Probability']
                subj2 = ['EASP', 'Practical Research 1']
                subj3 = ['Introduction to World Religions', 'Discipline and Ideas in the Applied Social Sciences']
                print(Fore.MAGENTA + 'LIST OF SUBJECTS FOR SECOND SEMESTER')
                print(Fore.RED + 'CORE SUBJECTS')
                for core in subj1:
                    print(Fore.CYAN + core)
                print(Fore.RED + 'APPLIED SUBJECTS')
                for core2 in subj2:
                    print(Fore.CYAN + core2)
                print(Fore.RED + 'SPECIALIZED SUBJECTS')
                for core3 in subj3:
                    print(Fore.CYAN + core3)
                student()
        elif strand == 'A' or strand == 'a':
            comm = input('Press [1] to View subjects for 1st Semester\nPress [2] to View subjects for 2nd Semester\n:')
            if comm == '1':
                subj1 = ['21st Century Literature', 'Earth Science', 'General Mathematics', 'Komunikasyon at Pananaliksik', 'Oral Communication', 'Physical Education 1']
                subj2 = ['Empowerment Technologies']
                subj3 = ['Applied Economics', 'Bussines Math']
                print(Fore.MAGENTA + 'LIST OF SUBJECTS FOR FIRST SEMESTER')
                print(Fore.RED + 'CORE SUBJECTS')
                for core in subj1:
                    print(Fore.CYAN + core)
                print(Fore.RED + 'APPLIED SUBJECTS')
                for core2 in subj2:
                    print(Fore.CYAN + core2)
                print(Fore.RED + 'SPECIALIZED SUBJECTS')
                for core3 in subj3:
                    print(Fore.CYAN + core3)
                student()
            elif comm == '2':
                subj1 = ['Physical Science', 'Pagbasa at Pagsusuri', 'Personal Development', 'PE 2', 'Reading and Writing', 'Statistics and Probability']
                subj2 = ['EASP', 'Practical Research 1']
                subj3 = ['No Subject']
                print(Fore.MAGENTA + 'LIST OF SUBJECTS FOR SECOND SEMESTER')
                print(Fore.RED + 'CORE SUBJECTS')
                for core in subj1:
                    print(Fore.CYAN + core)
                print(Fore.RED + 'APPLIED SUBJECTS')
                for core2 in subj2:
                    print(Fore.CYAN + core2)
                print(Fore.RED + 'SPECIALIZED SUBJECTS')
                for core3 in subj3:
                    print(Fore.CYAN + core3)
                student()
    elif comm == '12':
        strand = input('Press [S] for STEM\nPress [H] for HUMMS\nPress [A] for ABM\n:')
        if strand == 's' or strand == 'S':
            comm = input('Press [1] to View subjects for 1st Semester\nPress [2] to View subjects for 2nd Semester\n:')
            if comm == '1':
                subj1 = ['Contemporary Philippine Arts', 'Introduction to Philosophy', 'PE 3']
                subj2 = ['Filipino sa Piling Larang', 'Practical Research 2']
                subj3 = ['General Chemistry 1', 'General Physics 1']
                print(Fore.MAGENTA + 'LIST OF SUBJECTS FOR FIRST SEMESTER')
                print(Fore.RED + 'CORE SUBJECTS')
                for core in subj1:
                    print(Fore.CYAN + core)
                print(Fore.RED + 'APPLIED SUBJECTS')
                for core2 in subj2:
                    print(Fore.CYAN + core2)
                print(Fore.RED + 'SPECIALIZED SUBJECTS')
                for core3 in subj3:
                    print(Fore.CYAN + core3)
                student()
            elif comm == '2':
                subj1 = ['Media Information Literacy', 'Physical Education 4', 'Understanding Culture,Society and Politics']
                subj2 = ['Entrepreneurship', 'Inquiries,Investigations and Immersion']
                subj3 = ['General Chemistry 2', 'General Physics 2', 'Work Immersion/Capstone Project']
                print(Fore.MAGENTA + 'LIST OF SUBJECTS FOR SECOND SEMESTER ')
                print(Fore.RED + 'CORE SUBJECTS')
                for core in subj1:
                    print(Fore.CYAN + core)
                print(Fore.RED + 'APPLIED SUBJECTS')
                for core2 in subj2:
                    print(Fore.CYAN + core2)
                print(Fore.RED + 'SPECIALIZED SUBJECTS')
                for core3 in subj3:
                    print(Fore.CYAN + core3)
                student()
        elif strand == 'h' or strand == 'H':
            comm = input('Press [1] to View subjects for 1st Semester\nPress [2] to View subjects for 2nd Semester\n:')
            if comm == '1':
                subj1 = ['Contemporary Philippine Arts', 'Introduction to Philosophy', 'PE 3']
                subj2 = ['Filipino sa Piling Larang', 'Practical Research 2']
                subj3 = ['Creative Writting', 'Community Engagement']
                print(Fore.MAGENTA + 'LIST OF SUBJECTS FOR FIRST SEMESTER')
                print(Fore.RED + 'CORE SUBJECTS')
                for core in subj1:
                    print(Fore.CYAN + core)
                print(Fore.RED + 'APPLIED SUBJECTS')
                for core2 in subj2:
                    print(Fore.CYAN + core2)
                print(Fore.RED + 'SPECIALIZED SUBJECTS')
                for core3 in subj3:
                    print(Fore.CYAN + core3)
                student()
            elif comm == '2':
                subj1 = ['Media Information Literacy', 'Physical Education 4', 'Understanding Culture,Society and Politics']
                subj2 = ['Entrepreneurship', 'Inquiries,Investigations and Immersion']
                subj3 = ['Creative NON - Fiction', 'Trend,Networks and Critical Thinking', 'Work Immersion']
                print(Fore.MAGENTA + 'LIST OF SUBJECTS FOR SECOND SEMESTER ')
                print(Fore.RED + 'CORE SUBJECTS')
                for core in subj1:
                    print(Fore.CYAN + core)
                print(Fore.RED + 'APPLIED SUBJECTS')
                for core2 in subj2:
                    print(Fore.CYAN + core2)
                print(Fore.RED + 'SPECIALIZED SUBJECTS')
                for core3 in subj3:
                    print(Fore.CYAN + core3)
                student()
        elif strand == 'A' or strand == 'a':
            comm = input('Press [1] to View subjects for 1st Semester\nPress [2] to View subjects for 2nd Semester\n:')
            if comm == '1':
                subj1 = ['Contemporary Philippine Arts', 'Introduction to Philosophy', 'PE 3']
                subj2 = ['Filipino sa Piling Larang', 'Practical Research 2']
                subj3 = ['Creative Writting', 'Community Engagement']
                print(Fore.MAGENTA + 'LIST OF SUBJECTS FOR FIRST SEMESTER')
                print(Fore.RED + 'CORE SUBJECTS')
                for core in subj1:
                    print(Fore.CYAN + core)
                print(Fore.RED + 'APPLIED SUBJECTS')
                for core2 in subj2:
                    print(Fore.CYAN + core2)
                print(Fore.RED + 'SPECIALIZED SUBJECTS')
                for core3 in subj3:
                    print(Fore.CYAN + core3)
                student()
            elif comm == '2':
                subj1 = ['Media Information Literacy', 'Physical Education 4', 'Understanding Culture,Society and Politics']
                subj2 = ['Entrepreneurship', 'Inquiries,Investigations and Immersion']
                subj3 = ['Creative NON - Fiction', 'Trend,Networks and Critical Thinking', 'Work Immersion']
                print(Fore.MAGENTA + 'LIST OF SUBJECTS FOR SECOND SEMESTER ')
                print(Fore.RED + 'CORE SUBJECTS')
                for core in subj1:
                    print(Fore.CYAN + core)
                print(Fore.RED + 'APPLIED SUBJECTS')
                for core2 in subj2:
                    print(Fore.CYAN + core2)
                print(Fore.RED + 'SPECIALIZED SUBJECTS')
                for core3 in subj3:
                    print(Fore.CYAN + core3)
                student()
    elif comm == 'x' or comm == 'X':
        print(Fore.MAGENTA + 'Thank you for Using Student Sections!')
    elif comm != '11' or comm != '12':
        print('Invalid Grade Level Please Input 11 or 12 Only to Access!')

def teacher():
    print(Fore.GREEN + '################################################################################')
    print(Fore.GREEN + '#WELCOME TO TEACHERS SCHOOL MANAGEMENT HERE YOU CAN EDIT SOME STUFF OF STUDENTS#')
    print(Fore.GREEN + '################################################################################')
    crud = input('Press [C] to Create Data\nPress [R] Read/View Data\nPress [U] to Update Data\nPress [D] to Delete Data\nPress [X] to Exit\n:')
    if crud == 'c' or crud == 'C':
        create()
        print(Fore.CYAN + 'Database Success Created!')
        teacher()
    elif crud == 'r' or crud == 'R':
        read()
        teacher()
    elif crud == 'u' or crud == 'U':
        update()
        teacher()
    elif crud == 'd' or crud == 'D':
        delete()
        teacher()
    elif crud == 'x' or crud == 'X':
        print(Fore.MAGENTA + 'Thank you for Using Teacher Management!')

def create():
    newdata = input(Fore.MAGENTA +'Enter Database to Create: ')
    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE IF NOT EXISTS "+ newdata +" (`Studentid` int(11) NOT NULL AUTO_INCREMENT,`name` varchar(255) NOT NULL,`grade` varchar(255) NOT NULL,`section` varchar(255) NOT NULL,`strand` varchar(255) NOT NULL,PRIMARY KEY (`Studentid`))")

def read():
    dbname = input(Fore.MAGENTA + 'Enter Database name to View or Read: ')
    query = "SELECT * FROM "+ dbname + ""
    cur = mydb.cursor()
    cur.execute(query)
    records = cur.fetchall()
    print("Number of records in the table: ", cur.rowcount)
    for row in records:
        print(Fore.CYAN + "Data ID : ", row[0])
        print(Fore.CYAN + "Student Name : ", row[1])
        print(Fore.CYAN + "Student Grade : ", row[2])
        print(Fore.CYAN + "Student Section : ", row[3])
        print(Fore.CYAN + "Student Strand : ", row[4])

def update():
    dbname = input(Fore.MAGENTA +'Enter Database name to update: ')
    name = input(Fore.MAGENTA +'Enter Student Name: ')
    grade = input(Fore.MAGENTA +'Enter Student Grade: ')
    section = input(Fore.MAGENTA +'Enter Student Section: ')
    strand = input(Fore.MAGENTA +'Enter Student Strand: ')
    query = "INSERT INTO "+ dbname + " (name, grade, section, strand) VALUES ('" + name + "', '" + grade + "', '" + section + "', '" + strand + "')"
    cur = mydb.cursor()
    cur.execute(query)
    mydb.commit()
    cur.close()
    print(Fore.CYAN + "Update Data Successfully!")

def delete():
    dtname = input(Fore.MAGENTA +'Enter Database name to delete data: ')
    sid = input(Fore.MAGENTA +'Enter Data ID to delete Data row: ')
    mycursor = mydb.cursor()
    sql = "DELETE FROM "+ dtname +" WHERE Studentid = "+ sid +" "
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, Fore.CYAN + "record(s) deleted")


def start():
    while loop:
        print(Fore.GREEN + '###########################################################################')
        print(Fore.GREEN + '#SCHOOL MANAGEMENT SYSTEM (SDLC - implementation) UCOS 1-1 AMABA MARCROSS!#')
        print(Fore.GREEN + '###########################################################################')
        comm = input(Fore.BLUE + 'Press [S] to login as Student\nPress [T] to login as Teacher\n:')
        if comm == 's' or comm == 'S':
            student()
        elif comm == 't' or comm == 'T':
            teacher()
        elif comm != 's' or comm != 'S' or comm != 't' or comm != 'T':
            print(Fore.BLUE + "INVALID INPUT PLEASE TRY AGAIN")

start()