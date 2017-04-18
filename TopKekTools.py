#Very Indivitual Tool
#Created By Jackel Contact @ Othernet #TopKek

import os, socket, sys, re, time, threading, logging

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
Starting_Anime = """
===========================================================================
###########################################################################
    *       *  """+bcolors.FAIL+"""..."""+bcolors.OKGREEN+"""     *          *          *   ... .. . .. ... |        #
*            """+bcolors.FAIL+""";::::;"""+bcolors.OKGREEN+"""          *          *         .............   \       #
        *  """+bcolors.FAIL+""";::::; :;"""+bcolors.OKGREEN+""" *             *           *   ..   ..  ..  *  '------#
    *    """+bcolors.FAIL+""";:::::'   :;"""+bcolors.OKGREEN+"""    *   *   *         *      ..  .....  ..           #
*       """+bcolors.FAIL+""";:::::;     ;."""+bcolors.OKGREEN+"""    *       """+bcolors.FAIL+"""0"""+bcolors.OKGREEN+"""   *      *      .........             #
   *   """+bcolors.FAIL+""",:::::'       ;"""+bcolors.OKGREEN+""" *     *   """+bcolors.FAIL+"""OOO\."""+bcolors.OKGREEN+"""   *     *   .. .. .. ..            #
-------"""+bcolors.FAIL+"""::::::;       ;"""+bcolors.OKGREEN+"""----------"""+bcolors.FAIL+"""OOOOO\."""+bcolors.OKGREEN+"""-----------------------------------#
       """+bcolors.FAIL+""";:::::;       ;         OOOOOOOO"""+bcolors.OKGREEN+"""                                   #
      """+bcolors.FAIL+""",;::::::;     ;'         / OOOOOOO"""+bcolors.OKGREEN+"""         _-_     _-_     _-_      #
    """+bcolors.FAIL+""";:::::::::`. ,,,;.        /  / DOOOOOO"""+bcolors.OKGREEN+"""      |RIP|   |RIP|   |RIP|     #
  """+bcolors.FAIL+""".';:::::::::::::::::;,     /  /     DOOOO"""+bcolors.OKGREEN+"""    /     \ /     \ /     \    #
 """+bcolors.FAIL+""",::::::;::::::;;;;::::;,   /  /        DOOO"""+bcolors.OKGREEN+"""   | ___ | | ___ | | ___ |    #
"""+bcolors.FAIL+""";`::::::`'::::::;;;::::: ,#/  /          DOOO"""+bcolors.OKGREEN+"""                             #
"""+bcolors.FAIL+""":`:::::::`;::::::;;::: ;::#  /            DOOO"""+bcolors.OKGREEN+"""                            #
"""+bcolors.FAIL+"""::`:::::::`;:::::::: ;::::# /              DOO"""+bcolors.OKGREEN+"""                            #
"""+bcolors.FAIL+"""`:`:::::::`;:::::: ;::::::#/               DOO"""+bcolors.OKGREEN+"""                            #
 """+bcolors.FAIL+""":::`:::::::`;; ;:::::::::##                OO"""+bcolors.OKGREEN+"""                            #
 """+bcolors.FAIL+"""::::`:::::::`;::::::::;:::#                OO"""+bcolors.OKGREEN+"""                            #
 """+bcolors.FAIL+"""`:::::`::::::::::::;'`:;::#                O"""+bcolors.OKGREEN+"""                             #
  """+bcolors.FAIL+"""`:::::`::::::::;' /  / `:#                """+bcolors.OKGREEN+"""                              #
   """+bcolors.FAIL+"""::::::`:::::;'  /  /   `#                """+bcolors.OKGREEN+"""                              #
==========================================================================#
###########################################################################
#            """+bcolors.WARNING+""" _,.-----.,_"""+bcolors.OKGREEN+"""                #"""+bcolors.FAIL+"""########"""+bcolors.OKGREEN+"""# /"""+bcolors.OKBLUE+""" To Those Tho Believe"""+bcolors.OKGREEN+"""#
#          """+bcolors.WARNING+""",-~           ~-."""+bcolors.OKGREEN+"""              #"""+bcolors.FAIL+"""######"""+bcolors.OKGREEN+"""# / """+bcolors.OKBLUE+"""In The Unkown And Un-"""+bcolors.OKGREEN+"""#
#        """+bcolors.WARNING+""",^___           ___^."""+bcolors.OKGREEN+"""             #"""+bcolors.FAIL+"""####"""+bcolors.OKGREEN+"""# | """+bcolors.OKBLUE+"""Founded, We Will Never"""+bcolors.OKGREEN+"""#
#      """+bcolors.WARNING+"""/~"   ~"   .   "~   "~ \ """+bcolors.OKGREEN+"""           #"""+bcolors.FAIL+"""####"""+bcolors.OKGREEN+"""# | """+bcolors.OKBLUE+"""Allow Those Who Stand """+bcolors.OKGREEN+"""#
#    """+bcolors.WARNING+""" Y  ,--._    I    _.--.    Y"""+bcolors.OKGREEN+"""           #"""+bcolors.FAIL+"""##"""+bcolors.OKGREEN+"""# / """+bcolors.OKBLUE+"""Before Us, To See Us """+bcolors.OKGREEN+"""###
#     """+bcolors.WARNING+""" | Y     ~-. | ,-~     Y | """+bcolors.OKGREEN+"""            ## | """+bcolors.OKBLUE+"""In Our Weakesst, We """+bcolors.OKGREEN+"""#####
#      """+bcolors.WARNING+"""| |        }:{        | | """+bcolors.OKGREEN+"""            ## | """+bcolors.OKBLUE+"""Want Them To Know We """+bcolors.OKGREEN+"""####
#      """+bcolors.WARNING+"""j l       / | \       ! l """+bcolors.OKGREEN+"""            ## | """+bcolors.OKBLUE+"""Came As Monsters, Tog-"""+bcolors.OKGREEN+""" ##
#   """+bcolors.WARNING+""".-~  (__,.--" .^. "--.,__)  ~-. """+bcolors.OKGREEN+"""         ## | """+bcolors.OKBLUE+"""ether We Can Run This """+bcolors.OKGREEN+"""###
#  """+bcolors.WARNING+"""(           / / | \ \           ) """+bcolors.OKGREEN+"""        ## | """+bcolors.OKBLUE+"""World, We Are Anonymous,"""+bcolors.OKGREEN+"""#
#   """+bcolors.WARNING+"""\.____,   ~  \/"\/  ~   .____,/ """+bcolors.OKGREEN+"""         ## | """+bcolors.OKBLUE+"""We Are Legion, We Do Not"""+bcolors.OKGREEN+"""#
#   """+bcolors.WARNING+""" ^.____                 ____.^  """+bcolors.OKGREEN+"""         ## | """+bcolors.OKBLUE+"""Forgive, We Do Not Forg-"""+bcolors.OKGREEN+"""#
#      """+bcolors.WARNING+""" | |T ~\  !   !  /~ T| |     """+bcolors.OKGREEN+"""         ## | """+bcolors.OKBLUE+"""et To Those Who Fell """+bcolors.OKGREEN+"""####
#       """+bcolors.WARNING+"""| |l   _ _ _ _ _   !| |     """+bcolors.OKGREEN+"""         ## | """+bcolors.OKBLUE+"""Under The Power Of Greed"""+bcolors.OKGREEN+"""#
#       """+bcolors.WARNING+"""| l \/V V V V V V\/ j |     """+bcolors.OKGREEN+"""         ##############################
#       """+bcolors.WARNING+"""l  \ \|_|_|_|_|_|/ /  l     """+bcolors.OKGREEN+"""         ## $$$$$$$$$$$$$$$$$$$$$$$$$$#
#        """+bcolors.WARNING+"""\  \[T T T T T TI/  /      """+bcolors.OKGREEN+"""        #"""+bcolors.FAIL+"""##"""+bcolors.OKGREEN+"""# $~~Expect~~~~~~~~~~~~~~~~#
#         """+bcolors.WARNING+"""\  `^-^-^-^-^-^'  /       """+bcolors.OKGREEN+"""       #"""+bcolors.FAIL+"""####"""+bcolors.OKGREEN+"""# $~~~~~~~~Us~~~~~~~~~~~~~#
#          """+bcolors.WARNING+"""\               /        """+bcolors.OKGREEN+"""       #"""+bcolors.FAIL+"""####"""+bcolors.OKGREEN+"""# $~~~~~~~~~~~@TopKek~~~~~#
#           """+bcolors.WARNING+"""\.           ,/         """+bcolors.OKGREEN+"""      #"""+bcolors.FAIL+"""######"""+bcolors.OKGREEN+"""# $~~~~~~~~~~~~~~<(o)>~~~#
#             """+bcolors.WARNING+""""^-.___,-^"           """+bcolors.OKGREEN+"""     #"""+bcolors.FAIL+"""########"""+bcolors.OKGREEN+"""# $$$$$$$$$$$$$$$$$$$$$$#
###########################################################################



"""


Help = """
Commands:
-h              Displays This Help Screen

Crunch          Create A Word List

atscan.start    Basic Atscan
                Will Run command 'proxychains atscan
                -t 'target' --sql --wp --lfi --ip --email'

chdir           Change Directory

server.start    Starts Server

client.start    Starts Client
      .list     Lists All Known Tested Connection's
      .listadd  Add Servers

refresh.screen  Refreshes Console Screen
"""

home      = os.getcwd()

stringset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def atscan_Run():
    global home
    os.chdir("Assets")
    os.system("python Atscan_UserFriendly.py")
    os.chdir(home)
    Running()

def StartingAnime():
    print str(Starting_Anime)
    time.sleep(5)
    Running()

def Client_SList():
    try:
        SLIST = open("SLIST.txt", "r")
        for line in SLIST:
            server_list == SLIST

        SLIST.close()
        print bcolors.OKBLUE + str(SLIST)

    except:
        print bcolors.FAIL + "Operation Failed Have You Created A List?"
        Main_Commands()


def Client_Start():
    try:
        os.system("python Client.py")

    except:
        print bcolors.WARNING + "Operation Failed Is It Installed"
        Main_Commands()

def Server_Start():
    try:
        os.system("python Server.py")

    except:
        print bcolors.WARNING + "Operation Failed Is It Installed?"
        Main_Commands()

def Main_Commands():
    print bcolors.ENDC + "CopyRight @ #TopKek"
    Main_Input = raw_input("["+socket.gethostname()+"]?:>> ")
    if Main_Input == str("-?"):
        print bcolors.ENDC + Help
        Main_Commands()

    elif Main_Input == str("server.start"):
        Server_Start()

    elif Main_Input == str("client.start"):
        Client_Start()

    elif Main_Input == str("client.list"):
        Client_SList()

    elif Main_Input == str("chdir"):
        print bcolors.ENDC + "["+socket.gethostname()+"]?:>>" +"Current Directory Is: "+os.getcwd()
        Directory_Input = raw_input("["+socket.gethostname()+"]"+bcolors.OKGREEN+"(Target Directory:)"+bcolors.ENDC+"?:>> ")
        print bcolors.OKBLUE + "["+socket.gethostname()+"]?:>> " +"Directory Entered: "+Directory_Input
        print bcolors.WARNING + "["+socket.gethostname()+"]?:>> Attmepting To Change To Directory..."
        os.chdir(str(Directory_Input))
        print bcolors.OKGREEN + "["+socket.gethostname()+"]?:>> Operation Successfull, Directory Changed To: "+os.getcwd()
        os.system("clear")
        Running()

    elif Main_Input == str("exit"):
        print bcolors.FAIL + "Then Bye Saucy Mother Fucking Cunt"
        sys.exit(1)

    elif Main_Input == str("refresh.screen"):
        Running()

    elif Main_Input == str("atscan"):
        atscan_Run()

    else:
        print bcolors.WARNING + "Invalid Command"
        Main_Commands()

def Running():
    print bcolors.HEADER + Banner
    print bcolors.OKBLUE + "CopyRight @ Jackel | #TopKek / Othernet"
    print bcolors.UNDERLINE + "Time: "+time.asctime()
    print bcolors.ENDC + "Directory: "+os.getcwd()
    print bcolors.WARNING + """
    Please Remember All Tools Enclosed Are For
            'Educational' Purposes Only
    """
    print bcolors.OKBLUE + "-? for help"
    print
    Main_Commands()

StartingAnime()
