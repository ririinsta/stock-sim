import requests
import os
import sys

#os.system("taskkill /f /pid " + sys.argv[1])
print("Hi")
main = requests.get("https://raw.githubusercontent.com/ririinsta/stock-sim/main/main.py")
os.remove("main.py")
print("Updated")
open("main.py", "wb").write(main.content)