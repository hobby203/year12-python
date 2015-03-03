##edward hobbs 12SM
## Imports ##
import csv ##module for reading csv files into arrayes, then writing back
import os ## useful for clearing screen & logs
import time ##for sleeping
import datetime ##for dates in log files
from menus import * ##imports user menus (hides them away so they don't take up 200 lines)
## Functions ##
def resizeWindow(): ##resizes window to fit menus better (aesthetic only)
    ##os.system("MODE CON COLS=61 LINES=40") ##For WINDOWS comment out as appropriate
    os.system("resize -s 40 61") ##For UNIX comment out as appropriate (only works in gnome-terminal)
    ##print "" ##if both are disabled for convenience at school
def wait(int): ##tells program to pause, allows user to read messages (int is given as a number)
    time.sleep(int)
def clear(): ##clears screen from old menus (aesthetics only again)
    ##os.system("cls") ##for windows
    os.system("clear") ## for unix
    ##print "" ##if both are disabled for convenience at school
def logger(cost,index,group,reward): ##logs student activity, but not teachers, takes values for the cost, student username, the user group and the reward they took
    now = datetime.datetime.now() ##finds time
    date = str(now.strftime("%Y-%m-%d %H:%M")) ##converts time to readable format
    logFile = "~/merits.log" ##tells program where the logfile is, can be changed more easily
    os.system("echo "+date+" "+group[index][0]+" bought "+reward+" for "+str(cost)+" merits >>"+logFile) ##adds transaction to log (not machine-readable)
def printer(message): ##function to print out menus, instead of using ""print "HUGE LONG THING" "" messages are  defined in menus.py
    clear()
    print message ##prints the message, which is defined when the function is called
def importStudents(): ##imports students csv into a array for python to read
    studentDetails=csv.reader(open("students.csv","rb")) ##opens the list of students
    students=[] ##makes a list for the csv data
    for user in studentDetails:
        students.append(user)    ##adds csv data into the list
    return students
def importTeachers(): ##imports teachers csv into a array for python to read
    teacherDetails=csv.reader(open("teachers.csv","rb")) ##opens the list of teachers
    teachers=[] ##makes a list for the csv data
    for user in teacherDetails:
        teachers.append(user)  ##adds csv data into the list
    return teachers
def firstMenu(): ##checks for whether or not a user is a teacher or pupil
    printer(loginOne)
    count = 0
    while True:
        menuChoice=raw_input("\033[1;33m: \033[1;m") ##asks user for input
        if menuChoice.lower() == "b":
            return students,False ##tells program the user is a student
        elif menuChoice.lower() == "a":
            return teachers,True ## tells program the user is a teacher
            loginLoop()
        else:
            print "\033[1;31mInvalid Input\033[1;m"
            count = count + 1
            if count == 8:        ## this part clears the screen 
                count = 0         ## after 8 invalid inputs
                printer(loginOne) ## for aesthetics
def loginLoop(): ##asks user for username & password
    resizeWindow() ##resizes terminal window to fit and look nicer
    group,userType = firstMenu() ##finds out if the user is a pupil/teacher
    while True:
        if userType:
            printer(teacherLogin)  ##prints teacher login banner
        else:
            printer(studentLogin) ##prints student login banner
        username=raw_input("\033[1;33mPlease Enter Your Username: \033[1;m") ##asks for username
        if username.upper() == "Q": ##checks for rogue value "Q"
            loginLoop() ##back to the first menu!
            break
        password=raw_input("\033[1;33mPlease Enter Your Password: \033[1;m") ##asks for password
        if username.upper() == "Q": ##checks for rogue value "Q"
            loginLoop() ##back to the first menu!
            break
        index = passCheck(username,password,group) ##checks to see if username is valid, then if the password is correct if it IS valid
        if index == -1: ##this will happen if the username or password were wrong
            print "\033[1;31mIncorrect Password / Username\033[1;m" ##tells the user so
            wait(1) ##gives user time to read the message
        else:
            mainMenu(index,group,userType) ##goes to main menu for the user, when the details are correct
            break ##stops the while loop
def findUser(username,group): ##checks for a valid username, taking the inputted username and the correct database
    for i in range(len(group)):
        if group[i][0] == username: ##checks to see if the 0th item in each row of the students/teachers array is the username given
            return i ##returns the row for the user
    return -1 ##will happen if the username isn't found
def passCheck(username,password,group): ##checks for a valid password, takes username and password that have been input and the correct database
    index = findUser(username,group) ##finds the line where the user is stored, if it was found taking their username and correct database
    if index == -1: ##this will happen if the user wasn't  found
        return -1 ##tells program the user wasn't there
    elif group[index][1] == password: ##checks if the password matches the one that is stored
        return index ##tells program where the user is in the file, and that the pass is correct
    else:
        return -1 ##tells program the password was wrong
def mainMenu(index,group,userType): ##main menu function, where the magic happens! takes the user's position in the csv, their group and if they're a teacher or a student
    if userType: ##checks if user is teacher
        run = lambda: teacherMenu(index,group,userType) ##assigns the teacher menu to "run" 
    else: ##means that the user is a student
        run = lambda: studentMenu(index,group,userType) ##assigns the teacher menu to "run"
    run() ##runs the menu, as defined above
def studentMenu(index,group,userType): ##will run if python recognises the user as a STUDENT taking their position in the csv, group and if they're a student/teacher
    while True:
        printer(studentMenuOne)
        print "\033[1;32mWelcome,",group[index][2],group[index][3],"\033[1;m" ##say hello! (full name of user)
        menuChoice = raw_input("\033[1;33m: \033[1;m") ##asks for input, in a lovely, minimal fashion
        if menuChoice.upper() == "A":
            balanceMenu(index,group) ##shows user their merit balance
        elif menuChoice.upper() == "B":
            redeemMerits(index,group) ##allows user to redeem merits against prizes
        elif menuChoice.upper() == "C":
            rewardPrices() ##shows user prices of rewards
        elif menuChoice.upper() == "D":
            changePass(index,group) ##allows user to change their password
        elif menuChoice.upper() == "E":
            saveDetails(userType)  ##saves any changes to the csv, and writes back to it
            loginLoop() ##goes back to the start of the program!
        else:
            print "\033[1;31mInvalid Input\033[1;m" ##tells the user they can't read 
            wait(0.5) ##waits for it to sink in
def teacherMenu(index,group,userType): ##will run if python recognises the user as a TEACHER
    while True:
        printer(teacherMenuOne)
        print "\033[1;32mWelcome,",group[index][2],group[index][3],"\033[1;m" ##say hello! (full name of user)
        menuChoice = raw_input("\033[1;33m: \033[1;m") ##asks user for input in a lovely minimal fashion
        if menuChoice.upper() == "A":
            changeMerits(index,True) ##allows user to ADD merits
        elif menuChoice.upper() == "B":
            changeMerits(index,False) ##allows user to REMOVE merits
        elif menuChoice.upper() == "C":
            changePass(index,group) ##allows user to change their password
        elif menuChoice.upper() == "D":
            wipeMerits(index,group)
        elif menuChoice.upper() == "E":
            addUser()
        elif menuChoice.upper() == "F":
            removeUser()
        elif menuChoice.upper() == "G":
            saveDetails(userType) ##saves any changes back to the csv
            loginLoop() ##back to the top!
        else:
            print "\033[1;31mInvalid Input\033[1;m" ##tells user they can't read
            wait(0.5) ##waits for it to sink in
def balanceMenu(index,group): ##shows STUDENTS their balance
    clear() ##clears the screen (usually done by printer(), but it's not used in this instance, so this is necessary)
    meritBalance = group[index][4] ##finds the user's balance in the row
    print """\033[1;36m
        *********************************************
        *                                           *
          YOUR MERIT BALANCE IS:""",meritBalance,"""
        *                                           *
        *********************************************\033[1;m """ ##prints their balance in a lovely little box
    raw_input("\033[1;32mPress Enter To Return\033[1;m") ##asks user to mash keys to go onwards
def rewardPrices():## lists reward prices
    while True:
        printer(meritCostsOne) ##prints out the first page of prices
        menuChoice = raw_input("\033[1;33m: \033[1;m") ##asks user for input
        if menuChoice.upper() == "A":
            printer(meritCostsTwo) ##prints the second page of merits
            menuChoice = raw_input("\033[1;33m: \033[1;m") ##asks for input again
            if menuChoice.upper() != "B": ##checks to see if the user has input "B"
                break ##goes back to the menu
        else:
            break ##stops the loop
def meritRedeemer(cost,index,group,reward): ##function for redeeming merits, takes input from "redeemMerits" 
    if int(group[index][4]) < cost: ##checks to see if the user's balance is large enough to buy their chosen item
        print "\033[1;31mSorry, You can't afford that!\033[1;m" ##tells the user they're far too ambitious
        wait(2) ##waits so the student can see they can't afford their desired prize
    else:
        group[index][4] = int(group[index][4]) - cost ##deducts the price of the prize from their balance
        logger(cost,index,group,reward) ##logs the transaction
        print "\033[1;32m\n You have bought: ",reward,"\n Please go to office to collect your reward\033[1;m" ##tells the user they've redeemed their merits
        wait(2) ##waits for the user to read the message
        return
def redeemMerits(index,group): ##asks the user which reward they'd like
    while True:
        printer(meritChoiceOne) ##prints the table of merits, and their code
        menuChoice = raw_input("\033[1;33m: \033[1;m") ##asks for user input
        if menuChoice.upper() == "A":
            meritRedeemer(20,index,group,"Pens") ##tells redeemer they want PENS
        elif menuChoice.upper() == "B":
            meritRedeemer(50,index,group,"Football") ##tells redeemer they want A FOOTBALL
        elif menuChoice.upper() == "C":
            meritRedeemer(100,index,group,"CD Voucher") ##tells redeemer they want MUSIC
        elif menuChoice.upper() == "D":
            meritRedeemer(100,index,group,"Memory Stick") ##tells redeemer they want MEMORY
        elif menuChoice.upper() == "E":
            meritRedeemer(110,index,group,"Ice Skating") ##tells the redeemer they want to SKATE
        elif menuChoice.upper() == "F":
            meritRedeemer(150,index,group,"Computer Game") ##tells the redeemer they want GAMES
        elif menuChoice.upper() == "G":
            meritRedeemer(250,index,group,"Driving Lesson") ##tells the redeemer they want TO DRIVE
        elif menuChoice.upper() == "H":
            meritRedeemer(300,index,group,"Digital Camera") ##tells the redeemer they want A CAMERA
        elif menuChoice.upper() == "I":
            printer(meritChoiceTwo) ##goes to the next page of merits, for the rich ones
            menuChoice = raw_input("\033[1;33m: \033[1;m")
            if menuChoice.upper() == "J":
                meritRedeemer(400,index,group,"MP3 Player") ##tells the redeemer they want to PLAY THEIR MUSIC
            elif menuChoice.upper() == "K":
                meritRedeemer(500,index,group,"Games Console") ##tells redeemer they want to PLAY THE GAMES
            else:
                printer(meritChoiceOne) ## goes back to the first page, and repeats
        else:
            break ##back to first menu
def changeMerits(index,option): ##function for teachers to add/remove merits from groups/individuals
    group = students
    while True:
        if option: ##checks if the user is adding merits
            printer(addScreen) ##shows the "adding" screen if it is
            menuType = "Add Merits To: " ## variable for input prompts
            meritType = "Add" ##same as above, variable for input prompts
        else: ##realises the user is removing merits
            printer(removeScreen) ##prints the "removing" screen
            menuType = "Remove Merits From: " ## variable for input prompts
            meritType = "Remove" ##same as above, variable for input prompts
        menuChoice = raw_input("\033[1;33m: \033[1;m") ##asks user for input
        success = False ##automatically assumes that the program will go wrong, how pessimistic
        if menuChoice.upper() == "A": 
            user = raw_input("\033[1;33mWho Would You Like To "+menuType+"\033[1;m") ##asks who the teacher wants to add/remove merits from
            meritAmount = raw_input("\033[1;33mHow Many Merits Do You Want To "+meritType+": \033[1;m") ##asks how many merits to add/remove
            if option == False: ##happens if the teacher selected to REMOVE merits
                try:
                    meritAmount = 0 - int(meritAmount) ##converts the merit amount to a minus number (saves having quadruplicate code)
                except ValueError:
                    print "\033[1;31mThat Was Not A Number!\033[1;m" ##tells the user they didn't input a number for the merit count
                    wait(1) ##waits for the user to read the message
            try: 
                for i in range(len(group)):
                    if group[i][0] == user: ##checks if entry is the desired user
                        group[i][4] = int(group[i][4]) + int(meritAmount) ##adds merits to their balance
                        success = True
                if success:
                    print "\033[1;32m Merit Balance Changed! \033[1;m" ##tells the user so
                    raw_input("\033[1;32m Press Enter To Continue...\033[1;m") ##asks them to mash the keyboard to carry on
                    saveDetails(False) ##saves student details
                    break ##stops the loop
                else:
                    print "\033[1;31m User Not Found!\033[1;m" ##happens if the program couldn't find the user
                    wait(1) ##waits for the user to read the error
            except ValueError:
                print "\033[1;31mThat Was Not A Number!\033[1;m" ##will happen if the user inputs a string rather than a number
                wait(1) ##waits for the user to read the message
        elif menuChoice.upper() == "B":
            subject = raw_input("\033[1;33mWhich Subject Would You Like To "+menuType+"\033[1;m") ##asks which subject needs merits adding/removing
            meritAmount = raw_input("\033[1;33mHow Many Merits Do You Want To "+meritType+": \033[1;m") ##how many merits?
            if option == False:
                try:
                    meritAmount = 0 - int(meritAmount) ##converts the merit amount to a minus number (saves having quadruplicate code)
                except ValueError:
                    print "\033[1;31mThat Was Not A Number!\033[1;m" ##tells the user they didn't input a number for the merit count
                    wait(1) ##waits for the user to read the message
            try:
                for i in range(len(students)):
                    if group[i][6]==subject or group[i][7]==subject or group[i][8]==subject or group[i][9]==subject or group[i][10]==subject: ##checks if student does a subject
                        group[i][4] = int(group[i][4]) + int(meritAmount) ##adds the merits if they do
                        success = True ##tells python someone does that subject!
                if success: ##happens if someone does the chosen subject
                    print "\033[1;32m Merit Balance Changed! \033[1;m" ##tells them the merits were changed!
                    raw_input("\033[1;32m Press Enter To Continue...\033[1;m") ##asks user to mash keyboard to continue
                    saveDetails(False) ## saves students new balance
                    break ##stops the loop
                else:
                    print "\033[1;31m Subject Not Found!\033[1;m" ##tells the user the subject doesn't exist
                    wait(1) ##waits for the user to read the message
            except ValueError:
                print "\033[1;31mThat Was Not A Number!\033[1;m" ##tells the user they didn't input a number for the merit count
                wait(1) ##waits for the user to read the message
        elif menuChoice.upper() == "C":
            formGroup = raw_input("\033[1;33mWhich Form Would You Like To "+menuType+"\033[1;m") ##asks user for a form to add/remove merits to/from
            meritAmount = raw_input("\033[1;33mHow Many Merits Do You Want To "+meritType+": \033[1;m") ##how many merits?
            if option == False:
                try:
                    meritAmount = 0 - int(meritAmount) ##negates the merits, if the teacher wanted to do so
                except ValueError:
                    print "\033[1;31mThat Was Not A Number!\033[1;m" ##tells the user they didn't input a number for the merit count
                    wait(1) ##waits for the user to read the message      
            try:
                for i in range(len(students)):
                    if group[i][5]==formGroup: ##checks if users are in the specified form
                        group[i][4] = int(group[i][4]) + int(meritAmount) ## adds the merits to the user
                        success  = True ##tells python that form exists, and it has people in it!
                if success: ##checks if the form existed
                    print "\033[1;32m Merit Balance Changed! \033[1;m" ##tells user the merits were added
                    raw_input("\033[1;32m Press Enter To Continue...\033[1;m") ##asks them to mash the keyboard to continue
                    saveDetails(False) ##saves students new balance
                    break ##stops the loop
                else:
                    print "\033[1;31m Form Not Found!\033[1;m" ##tells the user that form didn't exist
                    wait(1) ##waits for the user to read the message
            except ValueError:
                print "\033[1;31mThat Was Not A Number!\033[1;m" ##tells the user they didn't input a number for the merits 
                wait(1) ##waits for them to read the message
        else: ##will happen if the user wants to  go back to the menu
            break ##stops the loop
def changePass(index,group): ##function for changing password
    while True:
        printer(passMenu) ##prints menu
        oldPass = raw_input("\033[1;33mPlease Enter Your Old Password: \033[1;m") ##asks for old password
        if group[index][1] == oldPass:
            newPass = raw_input("\033[1;33mPlease Enter Your New Password: \033[1;m") ##asks for new pass twice
            newPassCheck = raw_input("\033[1;33mPlease Enter That Again: \033[1;m")   ##to verify there aren't any typos etc.
            if newPass == newPassCheck: ##makes sure the passwords matched
                group[index][1] = newPass ##changes the password
                print "\033[1;32m\n Pass Succesfully Changed!\033[1;m" ##tells the user
                raw_input("\033[1;33m\n Press any key to continue..\033[1;m") ##asks for input
                break
            else: ##if they didn't match
                print "\033[1;31m\n Those Didn't Match!\033[1;m" ##says the passes didn't match
                wait(1.0) ##waits
        else: ##if incorrect pass
            print "\033[1;31m\n Incorrect Password\033[1;m" ##tells the user
            wait(1.0) ##waits
def saveDetails(userType): ##function to save the details into the csv
    if userType: ##checks if they're a teacher
        database = "teachers.csv" ##tells python it needs the teachers.csv
        group = teachers
    else: ##realises they're a student (or a teacher who's changed some student's merit balance)
        database = "students.csv" ##tells python it needs the students.csv
        group = students
    out = csv.writer(open(database,"wb"), delimiter=",") ##tells the csv writer where to put everything, and how to seperate it
    for i in range(len(group)):
        out.writerow(group[i]) ##writes all changes (and everything else for that matter) to the csv again!
def wipeMerits(index,group): ##function to reset all merit balances
    while True:
        printer(clearMenu) ##prints correct menu
        confirmation = raw_input("\033[1;33mAre You Sure? Yes/No \033[1;m") ##asks for confirmation
        if confirmation.lower() != "yes": ##checks if they wanted to 
            break
        else:
            username = group[index][0] ## finds the teacher's username
            password=raw_input("\033[1;33mPlease Enter Your Password: \033[1;m") ##asks for password
            correctPass = passCheck(username,password,group) ##checks to see if password matches  
            if correctPass == -1: ##will happen if it doesn't
                print "\033[1;31mIncorrect Password\033[1;m" ##tells the user so
                wait(1) ##waits for the message to sink in
            else: ##will happen when the user WAS found
                for i in range(len(students)): ##goes through list of students
                    students[i][4] = 0 ##sets their balance to 0
                print "\033[1;32m\n Balances Succesfully Changed!\033[1;m" ##tells the user the merits were reset
                saveDetails(False) ##saves changes to csv
                wait(2) ##waits for message to sink in
                break ##stops the loop
def addUser(): ##function for adding users to the program
    while True:
        printer(addUserMenu) ##prints the correct menu
        newUsername=raw_input("\033[1;33mPlease Enter Their Username: \033[1;m") ##asks for new user's username
        newFirstname=raw_input("\033[1;33mPlease Enter Their First Name: \033[1;m") ##asks for their first name
        newSurname=raw_input("\033[1;33mPlease Enter Their Surname: \033[1;m") ##asks for their second name
        newForm=raw_input("\033[1;33mPlease Enter Their Form: \033[1;m") ##asks for their form
        newSubjectOne=raw_input("\033[1;33mPlease Enter Their First Subject: \033[1;m")    ## these all
        newSubjectTwo=raw_input("\033[1;33mPlease Enter Their Second Subject: \033[1;m")   ## ask for
        newSubjectThree=raw_input("\033[1;33mPlease Enter Their Third Subject: \033[1;m")  ## which subjects
        newSubjectFour=raw_input("\033[1;33mPlease Enter Their Fourth Subject: \033[1;m")  ## the student
        newSubjectFive=raw_input("\033[1;33mPlease Enter Their Fifth Subject: \033[1;m")   ## takes
        newStudent=[newUsername,"school",newFirstname,newSurname,0,newForm,newSubjectOne,newSubjectTwo,newSubjectThree,newSubjectFour,newSubjectFive] ##puts the student into an array
        valid=True ##assumes that the teacher input everything correctly
        for i in range(len(newStudent)): ##first searches the whole array
            if newStudent[i]=="": ##makes sure there are no empty fields
                valid=False ##tells the program something was wrong
                error="\033[1;31mThere Was An Empty Field There \033[1;m" ##tells the user they missed a bit 
        for subject in newStudent[6:10]:
            if type(subject)!=str:
                valid=False
                error="\033[1;31mInvalid Subject!\033[1;m"
        if len(newStudent[5])!=2:
            valid=False ##tells the program something was wrong
            error="\033[1;31mInvalid Form Group!\033[1;m"
        if valid==False: ##will happen when the user input a wrong item
            print error ##prints the error defined above
            wait(1)
        else: ##otherwise
            students.append(newStudent) ##appends the array to the array of all the students
            print "\033[1;32m New Student Added! \033[1;m" ##tells the teacher so
            saveDetails(False) ##saves the students details to the csv
            wait(1) ##waits
            break ##stops the loop  
def removeUser(): ##function for removing a user
    while True:
        printer(removeUserMenu) ##prints the menu
        userToRemove = raw_input("\033[1;33mWhich User Would You Like To Remove: \033[1;m") ##asks for user to remove
        index = findUser(userToRemove,students) ##finds the user in the array
        if index == -1: ##happens if the user wasn't found
            print "\033[1;31mUser Not Found!\033[1;m" ##tells the person so
            wait(1) ##waits
            break ##stops the loop
        else: ##when the user WAS found
            print "\033[1;33mYou Chose",students[index][2],students[index][3] ##makes sure the teacher wanted to remove that user
            confirmation = raw_input("\n Is This Correct? Yes/No: \033[1;m") ##
            if confirmation.upper() == "YES": ##checks to see if they put yes
                students.pop(index) ##removes the user if they did
                saveDetails(False) ##saves the changes
                print "\033[1;32m User Removed!\033[1;m" ##tells the teacher so
                wait(1) ##waits
                break ##stops the loop
            else:
                print "\033[1;32m Remove User Aborted!\033[1;m" ##tells the user they didn't say yes
                wait(1) ##waits
                break ##stops the loop
## Main ##
students = importStudents() ##assigns the students array to "students"
teachers = importTeachers() ##assigns the teachers array to "teachers"
loginLoop() ##starts the ball rolling!

##colour codes##
##start with \033[1;$$m
## 31 = red
## 32 = green
## 33 = yellow
## 34 = blue
## end with \033[1;m
## eg '\033[1;36mTHIS IS IN CYAN\033[1;m' ##these are for aesthetics ONLY, but if you remove them, make sure you remove all of the code, otherwise it'll print stuff you don't want
## DOES NOT WORK IN WINDOWS. http://hastebin.com/fitupaxaru.py
