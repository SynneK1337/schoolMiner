import urllib.request
import zipfile
import os
from sys import argv
import configparser

print("[!] If possible, run this script as administrator for better hashrates.")
print("[!] Only CryptoNight-based coins are supported currently. You can mine XMR, ETN etc.")


class Miner():
    miner_url = 'https://github.com/nanopool/Claymore-XMR-CPU-Miner/releases/download/v4.0/Claymore.CryptoNote.CPU.Miner.v4.0.-.POOL.zip'

    def __init__(self):
        if "-c" or "--use-config" in argv:
            self.parse_cfg()
        else:
            self.interface()
        self.download()
        self.unzip()
        self.configure()

    def parse_cfg(self):
        cfg = configparser.ConfigParser()
        cfg.read("config.cfg")
        self.address = cfg['main']['address']
        self.pool = cfg['main']['pool']

    def interface(self):
        self.address = input("[?] Enter your address: ")
        if not self.address:
            self.address = "etnk5sbb4h2hqeQwoH19962Hr9Sx4XkR6LouYXEapges9rs3tQUL7CyegGnZEh7nEtYa26SUk237fhGiNpXdceMT1jYYD2B4kd"

        self.pool = input("[?] Enter your pool address: ")
        if not self.pool:
            self.pool = "pool.etn.spacepools.org:1337"

    def download(self):
        print('[+] Downloading the miner.')
        urllib.request.urlretrieve(self.miner_url, 'miner.zip')
        print('[+] Miner downloaded.')

    def unzip(self):
        with zipfile.ZipFile('miner.zip', 'r') as zip:
            zip.extractall('miner')
        print('[+] Miner unzipped.')

    def configure(self):
        os.chdir('miner')
        urllib.request.urlretrieve(
            "https://github.com/MikserCompany/quiet/releases/download/v1.01/Quiet.exe", "Quiet.exe")
        print("[+] Quiet.exe downloaded")
        miner_location = os.getcwd().replace('\\', '/')
        os.chdir(
            f'C:/Users/{os.getlogin()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup')
        with open('start.bat', 'w') as cfg:
            cfg.write(
                f'cd "{miner_location}" \nQuiet.exe NsCpuCNMiner64.exe -o {self.pool} -u {self.address} -t {os.getenv("NUMBER_OF_PROCESSORS")}')
            cfg.close()
        print("[+] Config generated.")
        os.system("start.bat")
        print("[+] Miner started.")


Miner()
