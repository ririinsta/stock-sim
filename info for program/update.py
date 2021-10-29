import requests
import os
import sys

os.system("taskkill /f /pid " + sys.argv[1])
main = requests.get("https://raw.githubusercontent.com/ririinsta/stock-sim/main/main.py")
os.remove("")