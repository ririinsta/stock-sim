import json
from typing import ItemsView
import yfn
import os
from os.path import exists
from datetime import date
import time
import click
import requests

version = "ghb0.0.02"
updateurl = "https://raw.githubusercontent.com/ririinsta/stock-sim/main/info%20for%20program/ver"

class Main():
    def firstRun():
        f = open('conf.cfg', 'a')
        f.write('{"firstRunDate": "' + str(date.today()) + '", "mainProfile": "main.prf"}')
        f.close()
    def startUp():
        if exists('./conf.cfg'):
            config = json.loads(open("conf.cfg", "r").readline())
            test = open(config['mainProfile']).readline()
            profile = json.loads(test)
            balance = profile['bal']
            portfolio = profile['port']
            return [balance, portfolio]
        else:
            Main.firstRun()
            return False
    def onClose(bal, port):
        if exists('./main.prf'):
            click.clear()
            os.remove('main.prf')
            f = open("main.prf", "a")
            x = {
                "profilename": "main",
                "bal": bal,
                "port": port
            }
            f.write(json.dumps(x))
            f.close()
        else: 
            f = open("main.prf", "a")
            x = {
                "profilename": "main",
                "bal": bal,
                "port": port
            }
            f.write(json.dumps(x))
            f.close()
    def mainMenu(bal, port):
        click.clear()
        print("1. Check Balance")
        print("2. Check Portfolio")
        print("3. Buy Stock")
        print("4. Sell Stock")
        print("5. Advance Day")
        print("6. test")
        print("i. Info")
        print("7. Close")

        awn = input("> ")
        Main.checkOption(awn, bal, port)
    def checkOption(awn, balance, portfolio):
        click.clear()
        if awn == "1":
            print("Balance: " + str(balance))
            input("Press any key to continue")
        if awn == "2":
            index = 0
            for item in portfolio:
                index = index + 1
                itemarray = item.split(",")
                print(str(index) + ". " + itemarray[2] + " " + itemarray[0] + " bought at " + itemarray[1] + " a piece")
            input()
        if awn == "3":
            print("What stock?")
            stock = input("> ")
            returned = Main.purchaseStock(stock, balance, portfolio)
            balance = returned[0]
            portfolio = returned[1]
        if awn == "4":
            among = input()
            for item in portfolio:
                if item.split()[0] == among:
                    print(item)
            print("")
            input("Press any key to continue")
        if awn == "5":
            input()
        if awn == "6":
            print(os.getpid())
            input()
        if awn == "i":
            print("Made by Riri")
            print("Version: " + version)
            print("Press U to check for updates")
            inp = input("Waiting for user input > ")
            if inp == "U":
                updatefile = requests.get(updateurl)
                open('tempupdfile.temp', 'wb').write(updatefile.content)
                ver = open('tempupdfile.temp', "r").readline()
                if ver == version:
                    print("Up to date!")
                    input("Press any key to continue")
                else:
                    print("Current Version: " + version)
                    print("New Version: " + ver)
                    input("Press any key to update.")
                    update = requests.get("https://raw.githubusercontent.com/ririinsta/stock-sim/main/info%20for%20program/update.py")
                    open('update.py', 'wb').write(update.content)
                    updatebat = requests.get("https://raw.githubusercontent.com/ririinsta/stock-sim/main/info%20for%20program/update.bat")
                    open('update.bat', 'wb').write(updatebat.content)
                    os.system(".\\update.bat " + str(os.getpid()))
                os.remove("tempupdfile.temp")
            if inp == "CSTM-PKG":
                ver = open('tempupdfile.temp', "r").readline()
                if ver == version:
                    print("Up to date!")
                    input("Press any key to continue")
                else:
                    print("Current Version: " + version)
                    print("New Version: " + ver)
                    input("Press any key to update.")
        if awn == "7":
            Main.onClose(balance, portfolio)
            exit()
        Main.mainMenu(balance, portfolio)
    def purchaseStock(stock, balance, portfolio):
        stonk = yfn.download(stock, period="1d")
        jsontest = r"" + stock + r"," +str(round(stonk['High'][str(date.today())], 2)) + r"," + r"1" + r""
        portfolio.append(jsontest)
        print(portfolio)
        input()
        return [balance, portfolio]

onrun = Main.startUp()
balance = 200
portfolio = []

if onrun == False:
    time.sleep(0)
else:
    balance = onrun[0]
    portfolio = onrun[1]

awn = Main.mainMenu(balance, portfolio)
