import json
import yfinance as yf
import os
from os.path import exists
from datetime import date
import time

class Main():
    def firstRun():
        f = open('conf.cfg', 'a')
        f.write('{"firstRunDate": "' + str(date.today()) + '", "mainProfile": "main.prf"}')
        f.close()
    def startUp():
        if exists('./conf.cfg'):
            config = json.loads(open("conf.cfg", "r").readline())
            profile = json.loads(open(config['mainProfile']).readline())
            balance = profile['balance']
            portfolio = profile['port']
            return [balance, portfolio]
        else:
            Main.firstRun()
            return False
    def onClose():
        if exists('./main.prf'):
            os.remove('main.prf')
            f = open('main.prf', 'a')
            f.write('{"profilename": "main", "port": ' + str(portfolio) + ', "balance": ' + str(balance) + '}')
            f.close
        else: 
            f = open('main.prf', 'a')
            f.write('{"profilename": "main", "port": ' + str(portfolio) + ', "balance": ' + str(balance) + '}')
            f.close
    def mainMenu(bal, port):
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
        if awn == "1":
            print("Balance: " + str(balance))
            input("Press any key to continue")
        if awn == "2":
            input()
        if awn == "3":
            print("What stock?")
            stock = input("> ")
        if awn == "4":
            input()
        if awn == "5":
            input()
        if awn == "6":
            print("Enter new balance")
            balance = int(input("> "))
        if awn == "7":
            Main.onClose()
            exit()
        Main.mainMenu(balance, portfolio)
onrun = Main.startUp()
balance = 200
portfolio = []

if onrun == False:
    time.sleep(0)
else:
    balance = onrun[0]
    portfolio = onrun[1]

awn = Main.mainMenu(balance, portfolio)
