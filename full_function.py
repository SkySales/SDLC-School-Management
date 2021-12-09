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
                query = "SELECT * FROM stem11"
                cur = mydb.cursor()
                cur.execute(query)
                records = cur.fetchall()
                print(Fore.MAGENTA + 'LIST OF SUBJECTS FOR FIRST SEMESTER')
                for row in records:
                    print(Fore.CYAN + "->", row[0])
                student()
            elif comm == '2':
                query = "SELECT * FROM stem11"
                cur = mydb.cursor()
                cur.execute(query)
                records = cur.fetchall()
                print(Fore.MAGENTA + 'LIST OF SUBJECTS FOR SECOND SEMESTER')
                for row in records:
                    print(Fore.CYAN + "->", row[1])
                student()
        elif strand == 'h' or strand == 'H':
            comm = input('Press [1] to View subjects for 1st Semester\nPress [2] to View subjects for 2nd Semester\n:')
            if comm == '1':
                query = "SELECT * FROM hums11"
                cur = mydb.cursor()
                cur.execute(query)
                records = cur.fetchall()
                print(Fore.MAGENTA + 'LIST OF SUBJECTS FOR FIRST SEMESTER')
                for row in records:
                    print(Fore.CYAN + "->", row[0])
                student()
            elif comm == '2':
                query = "SELECT * FROM hums11"
                cur = mydb.cursor()
                cur.execute(query)
                records = cur.fetchall()
                print(Fore.MAGENTA + 'LIST OF SUBJECTS FOR SECOND SEMESTER')
                for row in records:
                    print(Fore.CYAN + "->", row[1])
                student()
        elif strand == 'A' or strand == 'a':
            comm = input('Press [1] to View subjects for 1st Semester\nPress [2] to View subjects for 2nd Semester\n:')
            if comm == '1':
                query = "SELECT * FROM abm11"
                cur = mydb.cursor()
                cur.execute(query)
                records = cur.fetchall()
                print(Fore.MAGENTA + 'LIST OF SUBJECTS FOR FIRST SEMESTER')
                for row in records:
                    print(Fore.CYAN + "->", row[0])
                student()
            elif comm == '2':
                query = "SELECT * FROM abm11"
                cur = mydb.cursor()
                cur.execute(query)
                records = cur.fetchall()
                print(Fore.MAGENTA + 'LIST OF SUBJECTS FOR SECOND SEMESTER')
                for row in records:
                    print(Fore.CYAN + "->", row[1])
                student()
    elif comm == '12':
        strand = input('Press [S] for STEM\nPress [H] for HUMMS\nPress [A] for ABM\n:')
        if strand == 's' or strand == 'S':
            comm = input('Press [1] to View subjects for 1st Semester\nPress [2] to View subjects for 2nd Semester\n:')
            if comm == '1':
                query = "SELECT * FROM stem12"
                cur = mydb.cursor()
                cur.execute(query)
                records = cur.fetchall()
                print(Fore.MAGENTA + 'LIST OF SUBJECTS FOR FIRST SEMESTER')
                for row in records:
                    print(Fore.CYAN + "->", row[0])
                student()
            elif comm == '2':
                query = "SELECT * FROM stem12"
                cur = mydb.cursor()
                cur.execute(query)
                records = cur.fetchall()
                print(Fore.MAGENTA + 'LIST OF SUBJECTS FOR SECOND SEMESTER')
                for row in records:
                    print(Fore.CYAN + "->", row[1])
                student()
        elif strand == 'h' or strand == 'H':
            comm = input('Press [1] to View subjects for 1st Semester\nPress [2] to View subjects for 2nd Semester\n:')
            if comm == '1':
                query = "SELECT * FROM hums12"
                cur = mydb.cursor()
                cur.execute(query)
                records = cur.fetchall()
                print(Fore.MAGENTA + 'LIST OF SUBJECTS FOR FIRST SEMESTER')
                for row in records:
                    print(Fore.CYAN + "->", row[0])
                student()
            elif comm == '2':
                query = "SELECT * FROM hums12"
                cur = mydb.cursor()
                cur.execute(query)
                records = cur.fetchall()
                print(Fore.MAGENTA + 'LIST OF SUBJECTS FOR SECOND SEMESTER')
                for row in records:
                    print(Fore.CYAN + "->", row[1])
                student()
        elif strand == 'A' or strand == 'a':
            comm = input('Press [1] to View subjects for 1st Semester\nPress [2] to View subjects for 2nd Semester\n:')
            if comm == '1':
                query = "SELECT * FROM abm12"
                cur = mydb.cursor()
                cur.execute(query)
                records = cur.fetchall()
                print(Fore.MAGENTA + 'LIST OF SUBJECTS FOR FIRST SEMESTER')
                for row in records:
                    print(Fore.CYAN + "->", row[0])
                student()
            elif comm == '2':
                query = "SELECT * FROM abm12"
                cur = mydb.cursor()
                cur.execute(query)
                records = cur.fetchall()
                print(Fore.MAGENTA + 'LIST OF SUBJECTS FOR SECOND SEMESTER')
                for row in records:
                    print(Fore.CYAN + "->", row[1])
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

    mycursor.execute("CREATE TABLE IF NOT EXISTS "+ newdata +" (`subject` varchar(255) NOT NULL,`subject2` varchar(255) NOT NULL,`id` int(11) NOT NULL AUTO_INCREMENT,PRIMARY KEY (`id`))")

def read():
    dbname = input(Fore.MAGENTA + 'Enter Database name to View or Read: ')
    query = "SELECT * FROM "+ dbname + ""
    cur = mydb.cursor()
    cur.execute(query)
    records = cur.fetchall()
    print(Fore.RED + "LIST OF SUBJECTS FOR DATABASE "+ dbname +" IN FIRST SEMESTER")
    for row in records:
        print(Fore.CYAN + "", row[0])
    print(Fore.RED + "LIST OF SUBJECTS FOR DATABASE "+ dbname +" IN SECOND SEMESTER")
    for row in records:
        print(Fore.CYAN + "", row[1])

def update():
    dbname = input(Fore.MAGENTA +'Enter Database name to update: ')
    subj = input(Fore.MAGENTA +'Update 1st Sem Subject: ')
    subj2 = input(Fore.MAGENTA +'Update 2nd Sem Subject: ')
    query = "INSERT INTO "+ dbname + " (subject, subject2) VALUES ('" + subj + "', '" + subj2 + "')"
    cur = mydb.cursor()
    cur.execute(query)
    mydb.commit()
    cur.close()
    print(Fore.CYAN + "Update Data Successfully!")

def delete():
    dtname = input(Fore.MAGENTA +'Enter Database name to delete data: ')
    sid = input(Fore.MAGENTA +'Enter Data ID to delete Data row: ')
    mycursor = mydb.cursor()
    sql = "DELETE FROM "+ dtname +" WHERE id = "+ sid +" "
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
