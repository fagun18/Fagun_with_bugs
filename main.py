#!/usr/bin/python

import sys
import os
import time
import signal

yes = ['Y', 'y']
default_port_scan = "50"

# Function to handle CTRL+C
def sigint_handler(signum, frame):
    os.system("clear")
    print("CTRL+C detected!")
    print("\033[1;91mGood Bye!! Happy Hacking!!\033[1;m")
    sys.exit()

# Set up the CTRL+C signal handler
signal.signal(signal.SIGINT, sigint_handler)

# Clear the screen
os.system("clear")

# Logo function with your details
# Updated logo function with Fagun and Bug Emoji
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

# Main menu function
def menu():
    logo()
    print("""
        1-) Normal Scanning
        2-) Firewall Bypass
        3-) Vulnerability Scanning
        u-) Update
        0-) Exit
    """)

# Fagun_with_Bugs menu function
def fagun_with_bugs_menu():
    print("\n \033[1;91m Your output file is in your current directory \033[1;m")
    os.system("pwd")
    print(" \033[1;91m Your current directory \033[1;m")
    print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
    choice_donus = input("root""\033[1;91m@Fagun_with_Bugs:~$\033[1;m ")
    if choice_donus == "1":
        os.system("clear")
        fagun_with_bugs()
    elif choice_donus == "2":
        os.system("clear")
        print(" \033[1;91m@Good Bye !! Happy Hacking !!\033[1;m")
        sys.exit()
    else:
        print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
        time.sleep(2)
        fagun_with_bugs()

# Vulnerability Scanning function
def vul():
    print("Starting Vulnerability Scanning...")
    time.sleep(1)
    os.system("clear")
    logo()
    print("     Enter your IP address (0.0.0.0) or example.com")
    print("")
    vuln_target = input(" Enter Your Target: ")

    if not vuln_target:
        print("Please Enter a Target")
        print("\033[1;91mYou are grounded! Returning to the main menu...\033[1;m")
        time.sleep(2)
        os.system("clear")
        fagun_with_bugs()
    else:
        os.system("nmap -vv -sV --script vuln " + vuln_target + " -oN VulnerabilityScan-" + vuln_target + "-output")

    fagun_with_bugs()

# Rest of your functions...

# Fagun_with_Bugs main function
def fagun_with_bugs():
    menu()
    choice = input("root""\033[1;91m@Fagun_with_Bugs:~$\033[1;m ")
    os.system('clear')

    if choice == "1":
        udpscan()
    elif choice == "2":
        firewall()
    elif choice == "3":
        vul()
    elif choice == "u":
        update()
    elif choice == "00":
        credit()
    elif choice == "0":
        exit()
    elif choice == "":
        menu()
    else:
        print("Please enter one of the options in the menu.\nYou are directed to the main menu.")
        time.sleep(2)
        fagun_with_bugs()


# Fagun_with_Bugs main function
def fagun_with_bugs():
    menu()
    choice = input("root""\033[1;91m@Fagun_with_Bugs:~$\033[1;m ")
    os.system('clear')

    if choice == "1":
        udpscan()
    elif choice == "2":
        firewall()
    elif choice == "3":
        vul()
    elif choice == "u":
        update()
    elif choice == "00":
        credit()
    elif choice == "0":
        exit()
    elif choice == "":
        menu()
    else:
        print("Please enter one of the options in the menu.\nYou are directed to the main menu.")
        time.sleep(2)
        fagun_with_bugs()





# Vulnerability Scanning function
def vul():
    print("Starting Vulnerability Scanning...")
    time.sleep(1)
    os.system("clear")
    logo()
    print("     Enter your IP address (0.0.0.0) or example.com")
    print("")
    vuln_target = input(" Enter Your Target: ")

    if not vuln_target:
        print("Please Enter a Target")
        print("\033[1;91mYou are grounded! Returning to the main menu...\033[1;m")
        time.sleep(2)
        os.system("clear")
        Fagun_with_Bugs()
    else:
        os.system("nmap -vv -sV --script vuln " + vuln_target + " -oN VulnerabilityScan-" + vuln_target + "-output")

    darkmenu()


def Fagun_with_Bugs():
    menu()
    choice = input("root""\033[1;91m@Fagun_with_Bugs:~$\033[1;m ")
    os.system('clear')

    if choice == "1":
        udpscan()
    elif choice == "2":
        firewall()
    elif choice == "3":
        vul()
    elif choice == "u":
        update()
    elif choice == "00":
        credit()
    elif choice == "0":
        exit()
    elif choice == "":
        menu()
    else:
        print("Please enter one of the options in the menu.\nYou are directed to the main menu.")
        time.sleep(2)
        Fagun_with_Bugs()


def update():
    print("This Tool is Only Available for Linux and Similar Systems. ")
    choiceupdate = input("Continue Y / N: ")
    if choiceupdate in yes:
        os.system("git clone https://github.com/fagun18/Fagun_with_Bugs.git")
        os.system("cd Fagun_with_Bugs ")
        os.system("python3 Fagun_with_Bugs.py")


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
                "nmap -vv -sU --top-ports=" + defaultportscan + " " + beshedef + " -oN UdpScan-" + beshedef + "-output")
        else:
            os.system("nmap -vv -sU --top-ports=" + topport5 + " " + beshedef + " -oN UdpScan-" + beshedef + "-output")

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
def firewall():
    print("Starting Firewall Bypass ")
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
                "nmap -vv --script=firewall-bypass --top-ports=" + default_port_scan + " " + onhedef + " -oN " + "firewallbypass-" + onhedef + "-output")
        else:
            os.system(
                "nmap -vv --script=firewall-bypass --top-ports=" + topport10 + " " + onhedef + " -oN " + "firewallbypass-" + onhedef + "-output")

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


def darkmenu():
    # Add the implementation of the darkmenu function here
    # You can leave it empty for now or add the desired functionality
    pass


Fagun_with_Bugs()
