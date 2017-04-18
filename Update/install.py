import os, time, sys

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

def install_me():
    sys.exit(1)

update_directory_a = "Assets/Atscan_UserFriendly.py"
update_directory_b = "Assets/Atscan_UF005alpha.py"
#DFD - Documents for deletion
DFD_1               = "SLIST.txt"
DFD_2               = "Asciii.txt"

print "Checking Home Directory..."
tempdir = open("dir1.txt", "r")
for line in tempdir:
    tmpdir = line

tempdir.close()
print bcolors.HEADER + "Temp Directory Set To:"+str(tmpdir)
print "File To Update: "+str(update_directory_a)
print "What File will Be Updated To: "+str(update_directory_b)
print bcolors.OKGREEN + "Files To Delete: "+bcolors.WARNING +str(DFD_1)+", "+str(DFD_2)
print bcolors.OKGREEN + "Do You Wish To Continue?...[Y/n]"
input_me = raw_input("[Update]?:>> ")
if input_me == str("y" or "Y"):
    os.system("mv Atscan_UF005alpha.py "+str(tmpdir)+"/Assets")
    os.chdir(str(tmpdir))
    os.system("rm SLIST.txt")
    os.system("rm Asciii.txt")
    os.chdir("Assets")
    os.system("rm Atscan_UserFriendly.py")
    os.chdir()
    install_me()

else:
    sys.exit(1)
