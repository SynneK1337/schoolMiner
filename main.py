#!/usr/bin/python
from download_miner import download

print("Welcome to schoolMiner\n"
      "Which coin you want to mine?\n"
      "Available Coins:\n"
      " - Ethereum (ETH)\n"
      " - Monero (XMR)\n"
      " - ZCash (ZEC)\n")
coin = input("Coin: ").upper()

if coin == "ZEC" or coin == "XMR":
    method = input("CPU or GPU? ").upper()
    if method == "GPU":
        method = input("AMD or NVIDIA?").upper()
    print(method, coin)
    download(coin, method)

elif coin == "ETH":
    download(coin, "GPU") 