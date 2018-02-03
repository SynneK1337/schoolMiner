#!/usr/bin/python
from download_miner import download
from unzip import unzip
from get_architecture import get_architecture

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
        method = input("AMD or NVIDIA? ").upper()
    filename = download(coin, method)

elif coin == "ETH": # Ethereum can be mined only by GPU :(
    filename = download(coin, "GPU") 

unzip(filename)

if filename.startswith('zec'):
    