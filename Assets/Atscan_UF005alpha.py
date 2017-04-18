import os, time, socket, sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

Help   = """
target      - Set Target
sql         - Toggle Sql Scan
lfi         - Toggle Lfi Scan
wp          - Toggle Wp Scan
port        - Set Port
port.scan   - Toggle Port scan
email       - Set Email
save        - Save Scan
tcp         - Set Tcp Scan ( port.scan must be True )
udp         - set Udp Scan ( port.scan must be True )
start       - Begin Scan
exit        - Exits Session
-h          - Displays This Help Screen
"""

Banner = bcolors.OKGREEN+"""

###########################################################################
###"""+bcolors.FAIL+"""@@@@@@@@@@        @@@@@@@@@@@@@  @@@@@    @@@@ @@@@@@@@@  @@@@@    @@"""+bcolors.OKGREEN+"""###
##"""+bcolors.FAIL+"""@@@@@@@@@@@ @@@    @@@@@@    @@@@ @@@@@   @@@@@ @@@    @@@ @@@@@   @@@@"""+bcolors.OKGREEN+"""##
#    """+bcolors.FAIL+"""@@@@@ @@@@@@@@@ @@@@@@    @@@@ @@@@@  @@@@@ @@@@    @@@ @@@@@  @@@@  """+bcolors.OKGREEN+"""#
#    """+bcolors.FAIL+"""@@@@@@@      @@@@@@@@@@@@@@@@  @@@@@@@@@@@  @@@@ @@@    @@@@@@@@@@@  """+bcolors.OKGREEN+"""#
#    """+bcolors.FAIL+"""@@@@@         @@@@@@@@         @@@@@   @@@@@ @@@@     @ @@@@@   @@@  """+bcolors.OKGREEN+"""#
##   """+bcolors.FAIL+"""@@@@@@@      @@@ @@@@@         @@@@@     @@@@ @@@@@  @@@@@@@@    @@@"""+bcolors.OKGREEN+"""##
###  """+bcolors.FAIL+"""@@@@@ @@@@@@@@@  @@@@@         @@@@@      @@@  @@@@@@@@ @@@@@     @"""+bcolors.OKGREEN+"""###
###########################################################################
"""

home                   = os.getcwd()
temp_home              = os.getcwd()
time                   = time.asctime()
host                   = socket.gethostname()

sql                    = True
lfi                    = False
wp                     = False
email                  = False
ip                     = False
admin                  = False

port                   = 80
target                 = "http://www.example.com"

def Running():
    global sql
    Main_Coms = raw_input(bcolors.HEADER+"["+bcolors.OKBLUE+str(host)+bcolors.HEADER+"]?:>>")
    if Main_Coms == str("-h"):
        print bcolors.OKBLUE + str(Help)
        Running()

    elif Main_Coms == str("clear"):
        os.system("clear")
        Main()

    elif Main_Coms == str("sql"):
        if sql == str("True"):
            sql == str("False")
            Main()

        elif sql == str("False"):
            sql == str("True")
            Main()

    elif Main_Coms == str("exit"):
        sys.exit(1)

    else:
        print bcolors.WARNING + "Operation Failed Due To :"+bcolors.OKGREEN+"'Invalid Command'"
        print bcolors.WARNING + "Returning..."
        time.sleep(2)
        os.system("clear")
        Running()

def Main():
    global home
    global temp_home
    global time
    global host
    global sql
    global lfi
    global wp
    global email
    global ip
    global admin
    global port
    global target
    print Banner
    print "###########################################################################"
    print bcolors.ENDC + " Variable                                    :                      Status "
    print bcolors.HEADER + "   SQL                                       :                      "+str(sql)
    print bcolors.OKBLUE + "   LFI                                       :                      "+str(lfi)
    print bcolors.OKGREEN +"   WordPress                                 :                      "+str(wp)
    print bcolors.ENDC + "   Admin Scan                                :                      "+str(admin)
    print bcolors.OKBLUE +"   Email Scan                                :                      "+str(email)
    print bcolors.HEADER + "   Ip Scan                                   :                      "+str(ip)
    print bcolors.OKGREEN + "   Port Set To                               :                      "+str(port)
    print bcolors.OKBLUE + "   Target Set To                             :                      "+str(target)
    print bcolors.ENDC + "   Directory Set To                          :"+str(home)
    print bcolors.HEADER + "   Temporary Directory Set To                :"+str(temp_home)
    print bcolors.OKBLUE + "   Time Set To                               :"+str(time)
    print bcolors.WARNING + "   Host Set To                               :"+str(host)
    print bcolors.OKGREEN + "###########################################################################"
    print bcolors.OKBLUE  + " Use '-h' For The Help Screen"
    Running()

Main()
