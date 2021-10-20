import json
import yfinance as yf
import os
from os.path import exists
from datetime import date

class Main():
    def firstRun():
        f = open('conf.cfg', 'a')
        f.write('{"firstRunDate", "' + str(date.today()) + '", "mainProfile": "main.prf"}')
        f.close()

    def startUp():
        if exists('./conf.cfg'):
            return True
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
    def mainMenu():
        print("1. Check Balance")
        print("2. Check Portfolio")
        print("3. Buy Stock")
        print("4. Sell Stock")
        print("5. Advance Day")
        print("6. test")

        awn = input("> ")
        return awn
    def checkOption(opt):
        if awn == "1":
            input()
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
onrun = Main.startUp()
balance = 200
portfolio = []

awn = Main.mainMenu()

Main.checkOption(awn)

Main.onClose()
