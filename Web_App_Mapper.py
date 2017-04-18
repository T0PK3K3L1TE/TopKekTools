import Queue, threading, os, urllib2, re, sys, time

class bcolors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'

threads       = 10

target        = ""
directory     = ""
filters       = [".jpg", ".gif", ".png", ".css"]

Banner        = """
###############################################
####________###___ __  ___ ___####__##___######
###|__   __| \|    \ \/   /    \ |  \/   /#####
######| | / \ | ___/     /| ___/_|      /######
######| | \_/ / | |  |\  \| |__/ /  |\  \######
######|_|\___/|_| |__| \__\_____/|__| \__\#####
###############################################
"""



print bcolors.HEADER + str(Banner)
print bcolors.BOLD   + str("CopyRight @ Jackel | #TopKek")
print bcolors.OKBLUE + str("""
Please Remember This Is For
 'Educational' Reason Only
""")
print bcolors.BOLD + "Use 'default' Allow The Default Filter And Directory"
print "Target: "+target
print "Directory: "+directory

Target_Input      = raw_input(bcolors.OKGREEN+"[@TopKek]("+bcolors.FAIL+"Target"+bcolors.OKGREEN+")?:>> ")
Direct_Input      = raw_input(bcolors.ENDC+"[@TopKek]("+bcolors.BOLD+"Directory:"+str(directory)+bcolors.ENDC+")?:>> ")
Filt_Input        = raw_input(bcolors.OKBLUE+"[@TopKek]("+bcolors.BOLD+"Filer?"+bcolors.ENDC+")?:>> ")
if Direct_Input   == str("default"):
    if Filt_Input == str("default"):
        target    == str(Target_Input)
        Main_Functions(target, directory, filters)

    else:
        target    == str(Target_Input)
        directory == str(Direct_Input)
        Main_Functions(target, directory, filters)

else:
    target        == str(Target_Input)
    directory     == str(Direct_Input)
    filter_set()

print bcolors.BOLD   + "Target Set To: "+bcolors.HEADER+str(Target_Input)
print bcolors.ENDC   + "Directory Set To: "+bcolors.HEADER+str(Direct_Input)
print bcolors.OKBLUE + """Filer Set To: ".jpg", ".gif", ".png", ".css" """
