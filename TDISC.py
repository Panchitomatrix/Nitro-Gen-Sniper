#discord library
import discord
from discord import *
import discord.ext
from discord.ext import *

#normal library
import urllib3
urllib3.disable_warnings()
import string
import random
import time
import os
import ctypes
import subprocess
import requests
import colorama
from colorama import *
import time
import threading
from threading import Thread
from requests.exceptions import ProxyError, SSLError, ConnectionError, InvalidProxyURL

#program start
colorama.init()

def entireprogram():
    print("""
██████╗░██╗░██████╗░█████╗░░█████╗░██████╗░██████╗░  ████████╗░█████╗░░█████╗░██╗░░░░░░██████╗
██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
██║░░██║██║╚█████╗░██║░░╚═╝██║░░██║██████╔╝██║░░██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░
██║░░██║██║░╚═══██╗██║░░██╗██║░░██║██╔══██╗██║░░██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗
██████╔╝██║██████╔╝╚█████╔╝╚█████╔╝██║░░██║██████╔╝  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝
╚═════╝░╚═╝╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░
    Please make sure to sub and like lmao""")
    print("""
    [1] Discord Nitro Generator
    [2] Discord Nitro Checker
    [3] Discord Nitro Generator & Checker (AUTOPILOT)
    [4] Discord Sniper
    [5] Exit
    """)
    choice = int(input("[?]: "))
    if choice == 1:
        #nitro gen
        codeLen = 16 #length of the code
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789" #what the code can contain 
        lp = int(input("Enter The Number Of Unchecked Codes You Need: "))
        k = open('unchcekedcodes.txt', 'w')#if the file doesnt exist, itll make one - w stands for write
        for i in range(lp):
            k.write("discord.gift/" + ''.join(random.choice(letters) for i in range(codeLen)) + '\n')
        k.close()
        os.system('cls')
        entireprogram()

    elif choice == 2:
        #checker
        k = input("Enter The Code To Check: ")
        url = 'https://discordapp.com/api/v6/entitlements/gift-codes/' + k + '?with_application=false&with_subscription_plan=true'
        s = requests.session()
        response = s.get(url)
        if 'subscription_plan' in response.text:
            print(Fore.GREEN + "[VALID CODE] " + Fore.RESET)
            time.sleep(2)
        elif 'Access denied' in response.text:
            print(Fore.YELLOW + "Proxy Problem" + Fore.RESET)
            time.sleep(2)
        else:
            print(Fore.RED + "[INVALID CODE] " + k + Fore.RESET)
            time.sleep(2)
        os.system('cls')
        entireprogram()
    
    elif choice == 3:
        #gen & checker autopilot
        _THREADS = int(input("Enter The Number Of Threads: "))
        os.environ["_THREADS"] = "0"
        banned = 0
        nitro_codes = 0
        start_time = time.time()

        def clearterminal():
            os.system('cls' if os.name == 'nt' else 'clear')

        def codeGenerator():
            codeLen = 16
            letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            return ''.join(random.choice(letters) for i in range(codeLen))

        def getProxy():
            global proxies
            proxies = [line.rstrip('\n') for line in open("proxy.txt")]
            return random.choice(proxies)

        def banProxy(pxy):
            global proxies, banned
            if proxies.__contains__(pxy):
                proxies.remove(pxy)
                banned = banned + 1
            else:
                pass

        def saveCode(code):
            file = open("nitro_codes.txt","a")
            file.write(code + "\n")
            nitro_codes = nitro_codes + 1

        def getRuntime():
            elapsed_time = time.time() - start_time
            return str(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))

        class masterThread(threading.Thread):
            def __init__(self):
                threading.Thread.__init__(self)
                self.tasks = []
            def run(self):
                global banned, nitro_codes
                raw_proxy = ""
                while True:
                    try:
                        current_code = codeGenerator()

                        url = 'https://discordapp.com/api/v6/entitlements/gift-codes/' + current_code + '?with_application=false&with_subscription_plan=true'
                        raw_proxy = getProxy()
                        proxy = {'https': 'https://' + raw_proxy}

                        s = requests.session()
                        response = s.get(url, proxies=proxy)
                        if 'subscription_plan' in response.text:
                            saveCode(current_code)
                            print(Fore.GREEN + "[VALID CODE] " + Fore.RESET + "Saved Working code: " + current_code)
                        elif 'Access denied' in response.text:
                            banProxy(raw_proxy)
                            print(Fore.YELLOW + "Check this proxy: " + raw_proxy)
                        else:
                            print(Fore.RED + "[INVALID CODE] " + Fore.RESET + current_code)
                    except ProxyError:
                        pass
                    except SSLError:
                        banProxy(raw_proxy)
                        pass
                    except ConnectionError:
                        banProxy(raw_proxy)
                        pass
                    except InvalidProxyURL:
                        banProxy(raw_proxy)
                        pass
                    else:
                        pass
                generation = 0
                generation+=1
                ctypes.windll.kernel32.SetConsoleTitleW("Codes Checked: " + str(generation) + " | Made With Love By TOG6#6666")
        threads = []
        for x in range(_THREADS):
            threads.append(masterThread())

        for thread in threads:
            thread.daemon = True
            thread.start()
            thr = int(os.environ["_THREADS"])
            os.environ["_THREADS"] = str(thr + 1)

        while True:
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                print("\n Quitting...")
                exit(0)

    elif choice == 4:
        client = commands.bot(self_bot=True)
        print("This is the discord sniper")
        token = input("Enter Token: ")
        
        @client.event
        async def on_connect():
            print("User Details: ")
            print("Username: " + str(client.user.name))
            print("UserDiscriminator: " + str(client.user.discriminator))
            print("User ID: " + str(client.user.id))
            l = len(client.guilds)
            print("Servers: " + str(l))
            print("Token: " + token)

        @client.event
        async def on_message(message):
            if 'https://discord.gift/' in message.content:
                print("Found a Nitro Code!")
                code = message.content.split('https://discord.gift/')[1].split(' ')[0]
                headers = {'Authorization': token, 'Content-Type': 'application/json', 'Accept': 'application/json'}
                json = {
                    'channel_id': None,
                    'payment_source_id': None
                }
                r = requests.post('https://discordapp.com/api/v6/entitlements/gift-codes/'+code+'/redeem', verify=False,headers=headers, json=json)
                if r.status_code == 200:
                    print(Fore.GREEN + "=> Successfully claimed Nitro with Code: "+code , "Posted By: ", (message.author.name +"#"+ message.author.discriminator))
                    try:
                        print(Fore.GREEN +"Posted in:", (message.channel.name) , "|" , (message.guild.name))
                    except:
                        print(Fore.GREEN +"In DMS!")
                else:
                    print(Fore.RED + "=> Code already claimed or not valid, Code is: " +code , "Posted By: ", (message.author.name +"#"+ message.author.discriminator))
                    try:
                        print(Fore.RED +"Posted in:", (message.channel.name) , "|" , (message.guild.name))
                    except:
                        print(Fore.RED +"IN DMS!")
            elif 'discord.gift/' in message.content:
                print("Found a Nitro Code!")
                code = message.content.split('https://discord.gift/')[1].split(' ')[0]
                headers = {'Authorization': token, 'Content-Type': 'application/json', 'Accept': 'application/json'}
                json = {
                    'channel_id': None,
                    'payment_source_id': None
                }
                r = requests.post('https://discordapp.com/api/v6/entitlements/gift-codes/'+code+'/redeem', verify=False,headers=headers, json=json)
                if r.status_code == 200:
                    print(Fore.GREEN + "=> Successfully claimed Nitro with Code: "+code , "Posted By: ", (message.author.name +"#"+ message.author.discriminator))
                    try:
                        print(Fore.GREEN +"Posted in:", (message.channel.name) , "|" , (message.guild.name))
                    except:
                        print(Fore.GREEN +"In DMS!")
                else:
                    print(Fore.RED + "=> Code already claimed or not valid, Code is: " +code , "Posted By: ", (message.author.name +"#"+ message.author.discriminator))
                    try:
                        print(Fore.RED +"Posted in:", (message.channel.name) , "|" , (message.guild.name))
                    except:
                        print(Fore.RED +"IN DMS!")
            elif 'discordapp.com/gifts/' in message.content:
                print("Found a Nitro Code!")
                code = message.content.split('https://discord.gift/')[1].split(' ')[0]
                headers = {'Authorization': token, 'Content-Type': 'application/json', 'Accept': 'application/json'}
                json = {
                    'channel_id': None,
                    'payment_source_id': None
                }
                r = requests.post('https://discordapp.com/api/v6/entitlements/gift-codes/'+code+'/redeem', verify=False,headers=headers, json=json)
                if r.status_code == 200:
                    print(Fore.GREEN + "=> Successfully claimed Nitro with Code: "+code , "Posted By: ", (message.author.name +"#"+ message.author.discriminator))
                    try:
                        print(Fore.GREEN +"Posted in:", (message.channel.name) , "|" , (message.guild.name))
                    except:
                        print(Fore.GREEN +"In DMS!")
                else:
                    print(Fore.RED + "=> Code already claimed or not valid, Code is: " +code , "Posted By: ", (message.author.name +"#"+ message.author.discriminator))
                    try:
                        print(Fore.RED +"Posted in:", (message.channel.name) , "|" , (message.guild.name))
                    except:
                        print(Fore.RED +"IN DMS!")

            elif 'https://discordapp.com/gifts/' in message.content:
                print("Found a Nitro Code!")
                code = message.content.split('https://discord.gift/')[1].split(' ')[0]
                headers = {'Authorization': token, 'Content-Type': 'application/json', 'Accept': 'application/json'}
                json = {
                    'channel_id': None,
                    'payment_source_id': None
                }
                r = requests.post('https://discordapp.com/api/v6/entitlements/gift-codes/'+code+'/redeem', verify=False,headers=headers, json=json)
                if r.status_code == 200:
                    print(Fore.GREEN + "=> Successfully claimed Nitro with Code: "+code , "Posted By: ", (message.author.name +"#"+ message.author.discriminator))
                    try:
                        print(Fore.GREEN +"Posted in:", (message.channel.name) , "|" , (message.guild.name))
                    except:
                        print(Fore.GREEN +"In DMS!")
                else:
                    print(Fore.RED + "=> Code already claimed or not valid, Code is: " +code , "Posted By: ", (message.author.name +"#"+ message.author.discriminator))
                    try:
                        print(Fore.RED +"Posted in:", (message.channel.name) , "|" , (message.guild.name))
                    except:
                        print(Fore.RED +"IN DMS!")

    elif choice == 5:
        x = 5
    
    else:
        print("invalid choice!")
        time.sleep(2)
        os.system('cls')
        entireprogram()

entireprogram()