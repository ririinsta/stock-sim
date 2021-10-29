import yfn as stonk
import json as jsn

stonks = stonk.download("AAPL", period="1d")
print(str(stonks))
x = {
    "profilename": "testing",
    "bal": "inf",
    "port": ["DOGE-USD,0.01,1"]
}
print (x)
print (jsn.dumps(x))