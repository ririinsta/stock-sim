import json
from typing import ItemsView
import yfn
import os
from os.path import exists
from datetime import date
import time
import click

class Main():
    def firstRun():
        f = open('conf.cfg', 'a')
        f.write('{"firstRunDate": "' + str(date.today()) + '", "mainProfile": "main.prf"}')
        f.close()
    def startUp():
        #click.clear()
        if exists('./conf.cfg'):
            config = json.loads(open("conf.cfg", "r").readline())
            print("Config loaded")
            test = open(config['mainProfile']).readline()
            print(test)
            profile = json.loads(test)
            print("Profile Loaded")
            balance = profile['balance']
            print("Balance Loaded " + str(balance) + " in wallet")
            portfolio = profile['port']
            print("Portfolio Loaded " + str(portfolio) + " array")
            return [balance, portfolio]
        else:
            Main.firstRun()
            return False
    def onClose(bal, port):
        if exists('./main.prf'):
            click.clear()
            #print('Removing Current Profile')
            os.remove('main.prf')
            #input()
            #print('done')
            f = open("main.prf", "a")
            #print('Making and Setting new profile')
            x = {
                "profilename": "main",
                "bal": bal,
                "port": port
            }
            f.write(json.dumps(x))
            f.close()
            #print('closing')
            #input()
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
            input()
        if awn == "5":
            input()
        if awn == "6":
            stonk = yfn.download("AAPL", period="1d")
            print(stonk)
            input()
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
