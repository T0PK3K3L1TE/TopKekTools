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
    update = os.path.exists("Updates")
    if update == True:
        current_version = open("Version.txt", "r")
        for line in current_version:
            cversion = line

        current_version.close()
        os.chdir("Updates")
        os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/Version.txt")
        update_version = open("Version.txt", "r")
        for line in update_version:
            uversion = line

        update_version.close()
        if str(cversion) == str(uversion):
            print bcolors.OKGREEN+"Version: "+str(cversion)
            print "Everything Up To Date"
            os.system("rm Version.txt")
            sys.exit(1)

        else:
            print bcolors.FAIL+"Checking For Possible Update Files."
            os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/UpdateDependencies.py")
            os.system("python UpdateDependencies.py")
            os.system("rm Version.txt")
            os.system("rm UpdateDependencies.py")
            sys.exit(1)

    elif update == False:
        os.system("make Updates")
        Main()

    else:
        print bcolors.WARNING + "Operation Failed"
        sys.exit(1)

Main()
