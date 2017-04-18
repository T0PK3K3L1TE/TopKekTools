import os, re, socket, time, sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

home   = os.getcwd()

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

def Main():

    global Banner
    print Banner
    print bcolors.HEADER + "Attempting To Locate Update Package '"+os.getcwd()+"/Update'... "
    update = os.path.exists("Update")
    if update == True:
        os.chdir("Update")
        print bcolors.OKBLUE + "Successfull Checking For Package Version..."
        version_io = open("Version.txt", "r")
        for line in version_io:
            version = line

        version_io.close()
        print bcolors.OKGREEN + "Version: "+str(version)
        print bcolors.OKBLUE + "Creating Install Assets..."
        tempdir = open("dir1.txt", "w")
        tempdir.write(home)
        tempdir.close()
        print bcolors.OKGREEN + "Created..."
        print bcolors.WARNING + "Attempting Package Install..."
        os.system("python install.py")
        print bcolors.OKGREEN + "Update Finished..."
        sys.exit(1)

    elif update == False:
        print bcolors.FAIL + "Could Not locate File"
        sys.exit(1)

    else:
        print bcolors.WARNING + "Operation Failed"
        sys.exit(1)

Main()
