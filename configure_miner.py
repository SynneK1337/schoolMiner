from os import chdir, getlogin
from multiprocessing import cpu_count
from platform import system as os

def configure(coin, method, arch, address):
    if os() == "Windows" and arch == 64:
        chdir(r'C:\Users\%s\miner' % getlogin())
        f = open('start.bat', 'w')

        #XMR
        if coin == "XMR":
            if method == "CPU":
                f.write("Quiet.exe miner64.exe -o pool.minexmr.com:4444 -u %s -p x -t %s" % address, cpu_count())

            if method == "AMD":
                f.write("Quiet.exe miner64.exe -xpool pool.minexmr.com:4444, -xwal %s, -xpsw x" % address)

            if method == "NVIDIA":
                f.write("Quiet.exe miner64.exe -o pool.minexmr.com:4444 -u %s -p x" % address)
        
        #ETH
        elif coin == "ETH":
            f.write("Quiet.exe miner64.exe -epool eu1.ethermine.org:4444 -ewal %s -ethi 8 -dcri 1 -mode 1" % address)
        #ZEC
        elif coin == "ZEC":
            if method == "CPU":
                f.write("Quiet.exe miner64.exe -l eu1-zcash.flypool.org:3333 -u %s.sch1 -p x -t %s" % address, cpu_count())

            elif method == "AMD":
                f.write("Quiet.exe miner64.exe -zpool eu1-zcash.flypool.org:3333 -zwal %s.sch1 -zpsw x -i 8" % address)
            
            elif method == "NVIDIA":
                f.write("Quiet.exe miner64.exe --server eu1-zcash.flypool.org --user %s.sch1 --pass x --port 3333")
        
        f.close()