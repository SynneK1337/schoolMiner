#!/usr/bin/python
import download_miner

print("Welcome to schoolMiner\n"
      "Which coin you want to mine?\n"
      "Available Coins:\n"
      " - Ethereum (ETH)\n"
      " - Monero (XMR)\n"
      " - ZCash (ZEC)\n")

coin = input("Coin: ")
coin = coin.upper()

if coin == "ZEC" or coin == "XMR":
    method = input("CPU or GPU? ")
    method = method.upper()

if coin == "ETH":
    download_miner.eth_gpu()

elif coin == "XMR" and method == "CPU":
    xmr.cpu()

elif coin == "XMR" and method == "GPU":
    xmr.gpu()

elif coin == "ZEC" and method == "CPU":
    zec.cpu()

elif coin == "ZEC" and method == "GPU":
    zec.gpu()
