##these are imported into the main program, i've seperated them into this
##module to make scrolling through the main easier http://hastebin.com/nepeniwode.pl
loginOne = """\033[1;36m
        *********************************************
        *                                           *
        * WELCOME TO GREENPARKS SCHOOL MERIT SYSTEM *
        *                                           *
        *  IF YOU ARE A TEACHER: PRESS "A"          *
        *                                           *
        *  IF YOU ARE A STUDENT: PRESS "B"          *
        *                                           *
        *********************************************\033[1;m """
studentLogin = """\033[1;36m
        *********************************************
        *                                           *
        *              STUDENT LOGIN                *
        *                                           *
        *    USE "Q" AS THE USERNAME TO GO BACK     *
        *                                           *
        ********************************************* \033[1;m""" ##these codes tell the terminal window what colour each character should be 
teacherLogin = """\033[1;36m
        *********************************************
        *                                           *
        *              TEACHER LOGIN                *
        *                                           *
        *    USE "Q" AS THE USERNAME TO GO BACK     *
        *                                           *
        ********************************************* \033[1;m"""
studentMenuOne = """\033[1;36m
        *********************************************
        *                                           *
        *               STUDENT MENU                *
        *                                           *
        *  PRESS "A" TO VIEW MERIT BALANCE          *
        *                                           *
        *  PRESS "B" TO REDEEM MERITS               *
        *                                           *
        *  PRESS "C" TO VIEW REWARD PRICES          *
        *                                           *
        *  PRESS "D" TO CHANGE PASSWORD             *
        *                                           *
        *  PRESS "E" TO LOGOUT                      *
        *                                           *
        *********************************************\033[1;m """ 
teacherMenuOne = """\033[1;36m
        *********************************************
        *                                           *
        *                TEACHER MENU               *
        *                                           *
        *  PRESS "A" TO ADD MERITS                  *
        *                                           *
        *  PRESS "B" TO REMOVE MERITS               *
        *                                           *
        *  PRESS "C" TO CHANGE PASSWORD             *
        *                                           *
        *  PRESS "D" TO WIPE MERITS                 *
        *                                           *
        *  PRESS "E" TO ADD A NEW USER              *
        *                                           *
        *  PRESS "F" TO REMOVE A USER               *
        *                                           *
        *  PRESS "G" TO LOG OUT                     *
        *                                           *
        *********************************************\033[1;m """
passMenu =  """\033[1;36m
        *********************************************
        *                                           *
        *             CHANGE PASSWORD               *
        *                                           *
        *********************************************\033[1;m """
addScreen = """\033[1;36m
        *********************************************
        *                                           *
        *    WHO WOULD YOU LIKE TO GIVE MERITS?     *
        *                                           *
        *    PRESS "A" FOR STUDENTS                 *
        *                                           *
        *    PRESS "B" FOR SUBJECT                  *
        *                                           *
        *    PRESS "C" FOR FORM GROUP               *
        *                                           *
        *    PRESS ANY OTHER KEY TO EXIT            *
        *                                           *
        *********************************************\033[1;m """
removeScreen = """\033[1;36m
        *********************************************
        *                                           *
        *    WHO WOULD YOU LIKE TO REMOVE MERITS    *
        *    FROM?                                  *
        *                                           *
        *    PRESS "A" FOR STUDENTS                 *
        *                                           *  
        *    PRESS "B" FOR SUBJECT                  *
        *                                           *
        *    PRESS "C" FOR FROM GROUP               *
        *                                           *
        *   PRESS ANY OTHER KEY TO EXIT             *
        *                                           *
        *********************************************\033[1;m """ 
meritCostsOne = """\033[1;36m
        *********************************************
        *                                           *
        *                 MERIT COSTS               *
        *                      |                    *
        *   SET OF PENS        |       25           *
        *                      |                    *
        *   FOOTBALL           |       50           *
        *                      |                    *
        *   CD VOUCHER         |       100          *
        *                      |                    *
        *   MEMORY STICK       |       100          *
        *                      |                    *
        *   ICE SKATING        |       110          *
        *                      |                    *
        *   COMPUTER GAME      |       150          *
        *                      |                    *
        *   DRIVING LESSON     |       250          *
        *                      |                    *
        *   DIGITAL CAMERA     |       300          *
        *                      |                    *
        *  PRESS "A" FOR PAGE 2                     *
        *                                           *
        *  PRESS ANY OTHER KEY TO EXIT              *
        *                                           *
        *********************************************\033[1;m """
meritCostsTwo = """\033[1;36m
        *********************************************
        *                                           *
        *                 MERIT COSTS               *
        *                      |                    *
        *   MP3 PLAYER         |       400          *
        *                      |                    *
        *   GAMES CONSOLE      |       500          *
        *                      |                    *
        *  PRESS "B" FOR PAGE 1                     *
        *                                           *
        *  PRESS ANY OTHER KEY TO EXIT              *
        *                                           *
        *********************************************\033[1;m """
meritChoiceOne = """\033[1;36m
        *********************************************
        *                                           *
        *       WHICH REWARD WOULD YOU LIKE?        *
        *                                           *
        *   PRESS "A" FOR SET OF PENS               *
        *                                           *
        *   PRESS "B" FOR FOOTBALL                  *
        *                                           *
        *   PRESS "C" FOR CD VOUCHER                *
        *                                           *
        *   PRESS "D" FOR MEMORY STICK              *
        *                                           *
        *   PRESS "E" FOR ICE SKATING               *
        *                                           *
        *   PRESS "F" FOR COMPUTER GAMES            *
        *                                           *
        *   PRESS "G" FOR DRIVING LESSONS           *
        *                                           *
        *   PRESS "H" FOR DIGITAL CAMERA            *
        *                                           *
        *   PRESS "I" FOR PAGE 2                    *
        *                                           *
        *   OR PRESS ANY OTHER KEY TO GO BACK       *
        *                                           *
        *********************************************\033[1;m """
meritChoiceTwo = """\033[1;36m
        *********************************************
        *                                           *
        *       WHICH REWARD WOULD YOU LIKE?        *
        *                                           *
        *   PRESS "J" FOR MP3 PLAYER                *
        *                                           *
        *   PRESS "K" FOR GAMES CONSOLE             *
        *                                           *
        *   OR PRESS ANY OTHER KEY TO GO BACK       *
        *                                           *
        *********************************************\033[1;m """
clearMenu = """\033[1;36m
        *********************************************
        *                                           *
        *            WIPING ALL MERITS              *
        *                                           *
        *********************************************\033[1;m """
addUserMenu = """\033[1;36m
        *********************************************
        *                                           *
        *           ADDING NEW STUDENT              *
        *                                           *
        *********************************************\033[1;m """
removeUserMenu = """\033[1;36m
        *********************************************
        *                                           *
        *          REMOVING OLD STUDENT             *
        *                                           *
        *********************************************\033[1;m """
