#!/usr/bin/python
import download_miner

print("Welcome to schoolMiner\n"
      "Which coin you want to mine?\n"
      "Available Coins:\n"
      " - Ethereum (ETH)\n"
      " - Monero (XMR)\n"
      " - ZCash (ZEC)\n")

coin = input("Coin: ").upper()

if coin == "ZEC" or coin == "XMR":
    method = input("CPU or GPU? ").upper()

if coin == "ETH":
    download_miner.eth_gpu()

elif coin == "XMR" and method == "CPU":
    download_miner.xmr_cpu()

elif coin == "XMR" and method == "GPU":
    gpu = input("NVIDIA or AMD? (Intel not supported): ").upper()
    if gpu == "AMD" or gpu == "NVIDIA":
        download_miner.xmr_gpu(gpu)

    else:
        print("Wrong input...")

elif coin == "ZEC" and method == "CPU":
    download_miner.zec_cpu()

elif coin == "ZEC" and method == "GPU":
    gpu = input("NVIDIA or AMD? (Intel not supported): ").upper()
    if gpu == "NVIDIA" or gpu == "AMD":
        download_miner.zec_gpu(gpu)

    else:
        print("Wrong input")

else:
    print("Something went wrong... :(")