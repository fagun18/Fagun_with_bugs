import sys
import os
import time
import signal
from time import sleep
from sys import argv
from platform import system
yes = ['Y','y']
defaultportscan = "50";


def darkmenu():
    print("\n \033[1;91m your output file is in your current directory \033[1;m")
    os.system("pwd")
    print(" \033[1;91m Your current directory \033[1;m")
    print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
    choicedonus = input("root""\033[1;91m@Fagun_with_Bugs:~$\033[1;m ")
    if choicedonus == "1":
        os.system("clear")
        Fagun_with_Bugs()
    if choicedonus == "2":
        os.system("clear")
        print(" \033[1;91m@Good Bye !! Happy Hacking !!\033[1;m")
        sys.exit()
    else:
        print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
        time.sleep(2)
        Fagun_with_Bugs()


def sigint_handler(signum, frame):
    os.system("clear")
    print("CTRL+C detected!")
    print(" \033[1;91mGood Bye !! Happy Hacking !!\033[1;m")
    sys.exit()


signal.signal(signal.SIGINT, sigint_handler)

os.system("clear")


def logo():
    print("""
('-.                                 .-') _        (`\ .-') /`        .-') _    ('-. .-.     .-. .-')                             .-')    
           ( OO ).-.                            ( OO ) )        `.( OO ),'       (  OO) )  ( OO )  /     \  ( OO )                           ( OO ).  
   ,------./ . --. /  ,----.    ,--. ,--.   ,--./ ,--,'      ,--./  .--.  ,-.-') /     '._ ,--. ,--.      ;-----.\  ,--. ,--.     ,----.    (_)---\_) 
('-| _.---'| \-.  \  '  .-./-') |  | |  |   |   \ |  |\      |      |  |  |  |OO)|'--...__)|  | |  |      | .-.  |  |  | |  |    '  .-./-') /    _ |  
(OO|(_\  .-'-'  |  | |  |_( O- )|  | | .-') |    \|  | )     |  |   |  |, |  |  \'--.  .--'|   .|  |      | '-' /_) |  | | .-')  |  |_( O- )\  \:` `.  
/  |  '--.\| |_.'  | |  | .--, \|  |_|( OO )|  .     |/      |  |.'.|  |_)|  |(_/   |  |   |       |      | .-. `.  |  |_|( OO ) |  | .--, \ '..`''.) 
\_)|  .--' |  .-.  |(|  | '. (_/|  | | `-' /|  |\    |       |         | ,|  |_.'   |  |   |  .-.  |      | '--'  /('  '-'(_.-'  |  '--'  | \       / 
  \|  |_)  |  | |  | |  '--'  |('  '-'(_.-' |  | \   |       |   ,'.   |(_|  |      |  |   |  | |  |      | '--'  /('  '-'(_.-'  |  '--'  | \       / 
   `--'    `--' `--'  `------'   `-----'    `--'  `--'       '--'   '--'  `--'      `--'   `--' `--'      `------'   `-----'      `------'   `-----'  


     \033[1;92mFagun\033[0m 🐞 with \033[1;92mBugs\033[0m
    """)



def menu():
    logo()
    print("""
        1-) Fagun Normal Scanning
        2-) Fagun Firewall Scanning
        3-) Fagun Vulnerability Scanning
        4-) Fagun SQA Testing Tools 
        u-) Update
        00-) Contact with Me 
        0-) Exit
        """)


def Fagun_with_Bugs():
    menu()

    choice = input("root""\033[1;91m@Fagun_with_Bugs:~$\033[1;m ")

    os.system('clear')
    if choice == "1":
        dscan()
    elif choice == "2":
        firewall()
    elif choice == "3":
        vul()
    elif choice == "4":
        sqa()
    elif choice == "u":
        update()
    elif choice == "00":
        credit()
    elif choice == "0":
        exit()
    elif choice == "":
        menu()
    else:
        print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
        time.sleep(2)
        Fagun_with_Bugs()


def dscan():
    os.system("clear")
    logo()
    print("""
        1-) Fagun Default Scan
        2-) Fagun Host Discovery
        3-) Fagun Port(SYN) Scan
        4-) Fagun Port(TCP) Scan
        5-) Fagun Port(UDP) Scan
        6-) Fagun Null scan (-sN)
        7-) Fagun FIN scan (-sF)
        8-) Fagun OS Analysis and Version Discovery
        9-) Fagun Nmap Script Engineering (default)
        00-) Back to Menu
        """)

    choicedscan = input("root""\033[1;91m@DScan:~$\033[1;m ")
    os.system('clear')
    if choicedscan == "1":
        os.system('clear')
        ds()
    if choicedscan == "2":
        os.system('clear')
        hd()
    if choicedscan == '3':
        os.system('clear')
        synscan()
    if choicedscan == "4":
        os.system('clear')
        tcpscan()
    if choicedscan == "5":
        os.system('clear')
        udpscan()
    if choicedscan == "6":
        os.system('clear')
        nullscan()
    if choicedscan == "7":
        os.system('clear')
        finscan()
    if choicedscan == "8":
        os.system('clear')
        oavd()
    if choicedscan == "9":
        os.system('clear')
        nse()
    elif choicedscan == "00":
        Fagun_with_Bugs()


def firewall():
    os.system("clear")
    logo()
    print("""
        1-) Fagun Script Bypass (--script=firewall-bypass)
        2-) Fagun Data Length (--data-length <number> )
        3-) Fagun Smash (-ff)
        00-) Back to Menu
        """)

    choicefirewall = input("root""\033[1;91m@FirewallBypass:~$\033[1;m ")
    os.system('clear')
    if choicefirewall == "1":
        os.system('clear')
        sb()
    if choicefirewall == "2":
        os.system('clear')
        dl()
    if choicefirewall == '3':
        os.system('clear')
        smash()
    elif choicefirewall == "00":
        Fagun_with_Bugs()


def vul():
    os.system("clear")
    logo()
    print("""
        1-) Fagun Default Vuln Scan (--script vuln)
        2-) Fagun FTP Vuln Scan
        3-) Fagun SMB Vuln Scan
        4-) Fagun HTTP Vuln Scan
        5-) Fagun Special SQL Injection Vuln Scan
        6-) Fagun Stored XSS Vuln Scan
        7-) Fagun Dom Based XSS vuln Scan
        00-) Back to Menu
        """)

    choicevul = input("root""\033[1;91m@VulnerabilityScanning:~$\033[1;m ")
    os.system('clear')
    if choicevul == "1":
        os.system('clear')
        dvs()
    if choicevul == "2":
        os.system('clear')
        ftpvulscan()
    if choicevul == '3':
        os.system('clear')
        smbvulscan()
    if choicevul == "4":
        os.system('clear')
        httpvulscan()
    if choicevul == "5":
        os.system('clear')
        sqlvulscan()
    if choicevul == "6":
        os.system('clear')
        storedxssscan()
    if choicevul == "7":
        os.system('clear')
        domxssscan()
    elif choicevul == "00":
        Fagun_with_Bugs()

def sqa():
    os.system("clear")
    logo()
    print("""Coming Soon - follow on LinkedIn for get update: https://www.linkedin.com/in/mejbaur/
        00-) Back to Menu
        """)


    choicesqa = input("root""\033[1;91m@DScan:~$\033[1;m ")
    os.system('clear')

    if choicesqa == "00":
        Fagun_with_Bugs()


def update():
    print("This Tool is Only Available for Linux and Similar Systems. ")
    choiceupdate = input("Continue Y / N: ")
    if choiceupdate in yes:
        os.system("git clone https://github.com/fagun18/Fagun_with_bugs.git")
        os.system("cd Fagun_with_Bugs ")
        os.system("python3 fagun_with_bugs.py")


def ds():
    print(" Starting Default Scan...")
    time.sleep(1)
    os.system("clear")
    logo()
    print("     Enter your IP address (0.0.0.0) or example.com")
    print("")
    birhedef = input(" Enter Your Target: ")
    if not birhedef:
        print("Pls Enter Target")
        print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
        time.sleep(2)
        os.system("clear")
        Fagun_with_Bugs()
    else:
        topport1 = input("Top Port? Example: 10 or 50, Default 50:  ")
        if not topport1:
            os.system("nmap -vv --top-ports=" + defaultportscan + " " + birhedef + " -oN " + birhedef)
        else:
            os.system("nmap -vv --top-ports=" + topport1 + " " + birhedef + " -oN " + birhedef)

    darkmenu()


def hd():
    print(" Starting Host Discovery...")
    time.sleep(1)
    os.system("clear")
    logo()
    print("     Enter your IP address (0.0.0.0) or example.com")
    print("")
    ikihedef = input(" Enter Your Target: ")
    if not ikihedef:
        print("Pls Enter Target")
        print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
        time.sleep(2)
        os.system("clear")
        Fagun_with_Bugs()
    else:
        topport2 = input("Top Port? Example: 10 or 50, Default 50:  ")
        if not topport2:
            os.system(
                "nmap -vv -Pn --top-ports=" + defaultportscan + " " + ikihedef + " -oN HostD-" + ikihedef + "-output")
        else:
            os.system("nmap -vv -Pn --top-ports=" + topport2 + " " + ikihedef + " -oN HostD-" + ikihedef + "-output")

    darkmenu()


def synscan():
    print(" Starting Port(SYN) Scan...")
    time.sleep(1)
    os.system("clear")
    logo()
    print("     Enter your IP address (0.0.0.0) or example.com")
    print("")
    uchedef = input(" Enter Your Target: ")
    if not uchedef:
        print("Pls Enter Target")
        print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
        time.sleep(2)
        os.system("clear")
        Fagun_with_Bugs()
    else:
        topport3 = input("Top Port? Example: 10 or 50, Default 50:  ")
        if not topport3:
            os.system("nmap -vv -sS --top-ports=" + defaultportscan + " " + uchedef + " -oN " + uchedef + "-output")
        else:
            os.system("nmap -vv -sS --top-ports=" + topport3 + " " + uchedef + " -oN " + uchedef + "-output")

    darkmenu()


def tcpscan():
    print(" Starting Port(TCP) Scan...")
    time.sleep(1)
    os.system("clear")
    logo()
    print("     Enter your IP address (0.0.0.0) or example.com")
    print("")
    dorthedef = input(" Enter Your Target: ")
    if not dorthedef:
        print("Pls Enter Target")
        print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
        time.sleep(2)
        os.system("clear")
        Fagun_with_Bugs()
    else:
        topport4 = input("Top Port? Example: 10 or 50, Default 50:  ")
        if not topport4:
            os.system(
                "nmap -vv –sT --top-ports=" + defaultportscan + " " + dorthedef + " -oN TcpScan-" + dorthedef + "-output")
        else:
            os.system(
                "nmap -vv –sT --top-ports=" + topport4 + " " + dorthedef + " -oN TcpScan-" + dorthedef + "-output")

    darkmenu()


def udpscan():
    print(" Starting Port(UDP) Scan...")
    time.sleep(1)
    os.system("clear")
    logo()
    print("     Enter your IP address (0.0.0.0) or example.com")
    print("")
    beshedef = input(" Enter Your Target: ")
    if not beshedef:
        print("Pls Enter Target")
        print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
        time.sleep(2)
        os.system("clear")
        Fagun_with_Bugs()
    else:
        topport5 = input("Top Port? Example: 10 or 50, Default 50:  ")
        if not topport5:
            os.system(
                "nmap -vv –sU --top-ports=" + defaultportscan + " " + beshedef + " -oN UdpScan-" + beshedef + "-output")
        else:
            os.system("nmap -vv –sU --top-ports=" + topport5 + " " + beshedef + " -oN UdpScan-" + beshedef + "-output")

    darkmenu()


def nullscan():
    print(" Null scan (-sN)")
    time.sleep(1)
    os.system("clear")
    logo()
    print("     Enter your IP address (0.0.0.0) or example.com")
    print("")
    altihedef = input(" Enter Your Target: ")
    if not altihedef:
        print("Pls Enter Target")
        print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
        time.sleep(2)
        os.system("clear")
        Fagun_with_Bugs()
    else:
        topport6 = input("Top Port? Example: 10 or 50, Default 50:  ")
        if not topport6:
            os.system(
                "nmap -vv -sN --top-ports=" + defaultportscan + " " + altihedef + " -oN NullScan-" + altihedef + "-output")
        else:
            os.system(
                "nmap -vv -sN --top-ports=" + topport6 + " " + altihedef + " -oN NullScan-" + altihedef + "-output")

    darkmenu()


def finscan():
    print(" FIN scan (-sF)")
    time.sleep(1)
    os.system("clear")
    logo()
    print("     Enter your IP address (0.0.0.0) or example.com")
    print("")
    yedihedef = input(" Enter Your Target: ")
    if not yedihedef:
        print("Pls Enter Target")
        print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
        time.sleep(2)
        os.system("clear")
        Fagun_with_Bugs()
    else:
        topport7 = input("Top Port? Example: 10 or 50, Default 50:  ")
        if not topport7:
            os.system(
                "nmap -vv -sF --top-ports=" + defaultportscan + " " + yedihedef + " -oN FinScan-" + yedihedef + "-output")
        else:
            os.system(
                "nmap -vv -sF --top-ports=" + topport7 + " " + yedihedef + " -oN FinScan-" + yedihedef + "-output")

    darkmenu()


def oavd():
    print(" Starting OS Analysis and Version Discovery...")
    time.sleep(1)
    os.system("clear")
    logo()
    print("     Enter your IP address (0.0.0.0) or example.com")
    print("")
    sekizhedef = input(" Enter Your Target: ")
    if not sekizhedef:
        print("Pls Enter Target")
        print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
        time.sleep(2)
        os.system("clear")
        Fagun_with_Bugs()
    else:
        topport8 = input("Top Port? Example: 10 or 50, Default 50:  ")
        if not topport9:
            os.system(
                "nmap –sS -sV -O --top-ports=" + defaultportscan + " " + sekizhedef + " -oN Os-Version-" + sekizhedef + "output")
        else:
            os.system(
                "nmap –sS -sV -O --top-ports=" + topport8 + " " + sekizhedef + " -oN Os-Version-" + sekizhedef + "output")

    darkmenu()


def nse():
    print(" Starting Nmap Script Engineering...")
    time.sleep(1)
    os.system("clear")
    logo()
    print("     Enter your IP address (0.0.0.0) or example.com")
    print("")
    dokuzhedef = input(" Enter Your Target: ")
    if not dokuzhedef:
        print("Pls Enter Target")
        print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
        time.sleep(2)
        os.system("clear")
        Fagun_with_Bugs()
    else:
        topport9 = input("Top Port? Example: 10 or 50, Default 50:  ")
        if not topport9:
            os.system(
                "nmap -vv --script=default --top-ports=" + defaultportscan + " " + dokuzhedef + " -oN ScScan-" + dokuzhedef + "-output")
        else:
            os.system(
                "nmap -vv --script=default --top-ports=" + topport9 + " " + dokuzhedef + " -oN ScScan-" + dokuzhedef + "-output")

    darkmenu()


# firewall bypass
def sb():
    print("Starting Nmap Scripting Firewall Bypass ")
    time.sleep(1)
    os.system("clear")
    logo()
    print("     Enter your IP address (0.0.0.0) or example.com")
    print("")
    onhedef = input(" Enter Your Target: ")
    if not onhedef:
        print("Pls Enter Target")
        print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
        time.sleep(2)
        os.system("clear")
        Fagun_with_Bugs()
    else:
        topport10 = input("Top Port? Example: 10 or 50, Default 50:  ")
        if not topport10:
            os.system(
                "nmap -vv --script=firewall-bypass --top-ports=" + defaultportscan + " " + onhedef + " -oN " + "firewallbaypass-" + onhedef + "-output")
        else:
            os.system(
                "nmap -vv --script=firewall-bypass --top-ports=" + topport10 + " " + onhedef + " -oN " + "firewallbaypass-" + onhedef + "-output")

    darkmenu()


def dl():
    print("Starting Data Length ")
    time.sleep(1)
    os.system("clear")
    logo()
    print("     Enter your IP address (0.0.0.0) or example.com")
    print("")
    onbirhedef = input(" Enter Your Target: ")
    if not onbirhedef:
        print("Pls Enter Target")
        print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
        time.sleep(2)
        os.system("clear")
        Fagun_with_Bugs()
    else:
        topport11 = input("Top Port? Example 10 or 50, Default 50:  ")
        print("Append random data to sent packets")
        datalength = input("Number:")
        if not topport11:
            os.system(
                "nmap --data-string " + datalength + " --top-ports=" + defaultportscan + " " + onbirhedef + " -oN datalength-" + onbirhedef + "-output")
        else:
            os.system(
                "nmap ---data-string +" + datalength + " --top-ports=" + topport11 + " " + onbirhedef + " -oN datalength-" + onbirhedef + "output")

    darkmenu()


def smash():
    print("Smash (-ff) ")
    time.sleep(1)
    os.system("clear")
    logo()
    print("     Enter your IP address (0.0.0.0) or example.com")
    print("")
    onikihedef = input(" Enter Your Target: ")
    if not onikihedef:
        print("Pls Enter Target")
        print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
        time.sleep(2)
        os.system("clear")
        Fagun_with_Bugs()
    else:
        topport12 = input("Top Port? Example 10 or 50, Default 50:  ")
        if not topport12:
            os.system(
                "nmap -vv -ff --top-ports=" + defaultportscan + " " + onikihedef + " -oN " + "ff-" + onikihedef + "-output")
        else:
            os.system(
                "nmap -vv -ff --top-ports=" + topport12 + " " + onikihedef + " -oN " + "ff-" + onikihedef + "-output")

    darkmenu()


# Vulnerability Scan 'needs some tweaking'

def dvs():
    print("Default Vuln Scan ")
    time.sleep(1)
    os.system("clear")
    logo()
    print("     Enter your IP address (0.0.0.0) or example.com")
    print("")
    onuchedef = input(" Enter Your Target: ")
    if not onuchedef:
        print("Pls Enter Target")
        print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
        time.sleep(2)
        os.system("clear")
        Fagun_with_Bugs()
    else:
        topport13 = input("\033[92mTop Port? Example 10 or 50, Default 50:\033[0m;  ")
        if not topport13:
            os.system(
                "nmap -vv -sV -ff -Pn --top-ports=" + defaultportscan + " --script vuln " + onuchedef + " -oN " + "VulnScanDef-" + onuchedef + "-output")
        else:
            os.system(
                "nmap -vv -sV -ff -Pn --top-ports=" + topport13 + " --script vuln " + onuchedef + " -oN " + "VulnScanDef-" + onuchedef + "-output")

    darkmenu()


def ftpvulscan():
    print("FTP Vuln Scan ")
    time.sleep(1)
    os.system("clear")
    logo()
    print("     Enter your IP address (0.0.0.0) or example.com")
    print("")
    ondorthedef = input(" Enter Your Target: ")
    if not ondorthedef:
        print("Pls Enter Target")
        print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
        time.sleep(2)
        os.system("clear")
        Fagun_with_Bugs()
    else:
        topport14 = input("\033[92mTop Port? Example 10 or 50, Default 50:\033[0m;  ")
        if not topport14:
            os.system(
                "nmap -vv -sV -ff -Pn --top-ports=" + defaultportscan + " --script ftp* " + ondorthedef + " -oN " + "FTPvuln-" + ondorthedef + "-output")
        else:
            os.system(
                "nmap -vv -sV -ff -Pn --top-ports=" + topport14 + " --script ftp* " + ondorthedef + " -oN " + "FTPvuln-" + ondorthedef + "-output")

    darkmenu()


def smbvulscan():
    print("SMB Vuln Scan ")
    time.sleep(1)
    os.system("clear")
    logo()
    print("     Enter your IP address (0.0.0.0) or example.com")
    print("")
    onbeshedef = input(" Enter Your Target: ")
    if not onbeshedef:
        print("Pls Enter Target")
        print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
        time.sleep(2)
        os.system("clear")
        Fagun_with_Bugs()
    else:
        topport15 = input("\033[92mTop Port? Example 10 or 50, Default 50:\033[0m;  ")
        if not topport15:
            os.system(
                "nmap -vv -sV -ff -Pn --top-ports=" + defaultportscan + " --script smb* " + onbeshedef + " -oN " + "SMBvuln-" + onbeshedef + "-output")
        else:
            os.system(
                "nmap -vv -sV -ff -Pn --top-ports=" + topport15 + " --script smb* " + onbeshedef + " -oN " + "SMBvuln-" + onbeshedef + "-output")

    darkmenu()


def httpvulscan():
    print("HTTP Vuln Scan ")
    time.sleep(1)
    os.system("clear")
    logo()
    print("     Enter your IP address (0.0.0.0) or example.com")
    print("")
    onaltihedef = input(" Enter Your Target: ")
    if not onaltihedef:
        print("Pls Enter Target")
        print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
        time.sleep(2)
        os.system("clear")
        Fagun_with_Bugs()
    else:
        topport16 = input("\033[92mTop Port? Example 10 or 50, Default 50:\033[0m;  ")
        if not topport16:
            os.system(
                "nmap -vv -sV -ff -Pn --top-ports=" + defaultportscan + " --script smb* " + onaltihedef + " -oN " + "HTTPvuln-" + onaltihedef + "-output")
        else:
            os.system(
                "nmap -vv -sV -ff -Pn --top-ports=" + topport16 + " --script smb* " + onaltihedef + " -oN " + "HTTPvuln-" + onaltihedef + "-output")

    darkmenu()


def sqlvulscan():
    print("SQL Injection Vuln Scan ")
    time.sleep(1)
    os.system("clear")
    logo()
    print("     Enter your IP address (0.0.0.0) or example.com")
    print("")
    onyedihedef = input(" Enter Your Target: ")
    if not onyedihedef:
        print("Pls Enter Target")
        print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
        time.sleep(2)
        os.system("clear")
        Fagun_with_Bugs()
    else:
        topport17 = input("\033[92mTop Port? Example 10 or 50, Default 50:\033[0m;  ")
        if not topport17:
            os.system(
                "nmap -vv -sV -ff -Pn --top-ports=" + defaultportscan + " --script=http-sql-injection " + onyedihedef + " -oN " + "SQLvuln-" + onyedihedef + "-output")
        else:
            os.system(
                "nmap -vv -sV -ff -Pn --top-ports=" + topport17 + " --script=http-sql-injection " + onyedihedef + " -oN " + "SQLvuln-" + onyedihedef + "-output")

    darkmenu()


def storedxssscan():
    print("Stored XSS Vuln Scan ")
    time.sleep(1)
    os.system("clear")
    logo()
    print("     Enter your IP address (0.0.0.0) or example.com")
    print("")
    onsekizhedef = input(" Enter Your Target: ")
    if not onsekizhedef:
        print("Pls Enter Target")
        print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
        time.sleep(2)
        os.system("clear")
        Fagun_with_Bugs()
    else:
        topport18 = input("\033[92mTop Port? Example 10 or 50, Default 50:\033[0m;  ")
        if not topport18:
            os.system(
                "nmap -vv -sV -ff -Pn --top-ports=" + defaultportscan + " --script=http-stored-xss.nse " + onsekizhedef + " -oN " + "StoredXSSvuln-" + onsekizhedef + "-output")
        else:
            os.system(
                "nmap -vv -sV -ff -Pn --top-ports=" + topport18 + " --script=http-stored-xss.nse " + onsekizhedef + " -oN " + "StoredXSSvuln-" + onsekizhedef + "-output")

    darkmenu()


def domxssscan():
    print("DOM Based XSS Vuln Scan ")
    time.sleep(1)
    os.system("clear")
    logo()
    print("     Enter your IP address (0.0.0.0) or example.com")
    print("")
    ondokuzhedef = input(" Enter Your Target: ")
    if not ondokuzhedef:
        print("Pls Enter Target")
        print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
        time.sleep(2)
        os.system("clear")
        Fagun_with_Bugs()
    else:
        topport19 = input("\033[92mTop Port? Example 10 or 50, Default 50:\033[0m;  ")
        if not topport19:
            os.system(
                "nmap -vv -sV -ff -Pn --top-ports=" + defaultportscan + " --script=http-dombased-xss.nse " + ondokuzhedef + " -oN " + "DomBasedXSSvuln-" + ondokuzhedef + "-output")
        else:
            os.system(
                "nmap -vv -sV -ff -Pn --top-ports=" + topport19 + " --script=http-dombased-xss.nse " + ondokuzhedef + " -oN " + "DomBasedXSSvuln-" + ondokuzhedef + "-output")

    darkmenu()


def credit():
    print("""
('-.                                 .-') _        (`\ .-') /`        .-') _    ('-. .-.     .-. .-')                             .-')    
           ( OO ).-.                            ( OO ) )        `.( OO ),'       (  OO) )  ( OO )  /     \  ( OO )                           ( OO ).  
   ,------./ . --. /  ,----.    ,--. ,--.   ,--./ ,--,'      ,--./  .--.  ,-.-') /     '._ ,--. ,--.      ;-----.\  ,--. ,--.     ,----.    (_)---\_) 
('-| _.---'| \-.  \  '  .-./-') |  | |  |   |   \ |  |\      |      |  |  |  |OO)|'--...__)|  | |  |      | .-.  |  |  | |  |    '  .-./-') /    _ |  
(OO|(_\  .-'-'  |  | |  |_( O- )|  | | .-') |    \|  | )     |  |   |  |, |  |  \'--.  .--'|   .|  |      | '-' /_) |  | | .-')  |  |_( O- )\  \:` `.  
/  |  '--.\| |_.'  | |  | .--, \|  |_|( OO )|  .     |/      |  |.'.|  |_)|  |(_/   |  |   |       |      | .-. `.  |  |_|( OO ) |  | .--, \ '..`''.) 
\_)|  .--' |  .-.  |(|  | '. (_/|  | | `-' /|  |\    |       |         | ,|  |_.'   |  |   |  .-.  |      | '--'  /('  '-'(_.-'  |  '--'  | \       / 
  \|  |_)  |  | |  | |  '--'  |('  '-'(_.-' |  | \   |       |   ,'.   |(_|  |      |  |   |  | |  |      | '--'  /('  '-'(_.-'  |  '--'  | \       / 
   `--'    `--' `--'  `------'   `-----'    `--'  `--'       '--'   '--'  `--'      `--'   `--' `--'      `------'   `-----'      `------'   `-----'  


     \033[1;92mFagun\033[0m 🐞 with \033[1;92mBugs\033[0m
                ===================================== 
          NOTE : For Back To Menu Press 1 OR For Exit Press 2
       ==========================================================                                                                   
\033[1;m """)

    print("""
                 [!] LinkedIn: \033[1;91mhttps://www.linkedin.com/in/mejbaur/\033[1;m\n     
                 [!] Web Site: \033[1;91mhttps://mbfagun.blogspot.com\033[1;m\n   
                 [!] Github: \033[1;91mhttps://github.com/fagun18\033[1;m\n   
                 [!] Newsletter: \033[1;91mhttps://www.linkedin.com/newsletters/7049699805199020032/\033[1;m\n\n """)
    choicedonus = input("root""\033[1;91m@Credit:~$\033[1;m ")
    if choicedonus == "1":
        os.system("clear")
        Fagun_with_Bugs()
    if choicedonus == "2":
        os.system("clear")
        print(" \033[1;91mGood Bye !! Happy Hacking !!\033[1;m")
        sys.exit()
    else:
        print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
        time.sleep(2)
        Fagun_with_Bugs()


def exit():
    print(" \033[1;91mGood Bye !! Happy Hacking !!\033[1;m")
    sys.exit()


def rootcontrol():
    if os.geteuid() == 0:
        Fagun_with_Bugs()
    else:
        print("Please run it with root access.")
        sys.exit()


rootcontrol()
