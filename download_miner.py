from os import chdir, getlogin
from platform import system as os
import urllib.request

url = "http://127.0.0.1/" #Enter your HTTP Server here, soon


def download(coin, method):
    if os() == "Windows":
        print("OS is Windows")
        chdir(r'C:\Users\%s' % getlogin())
        if coin == "XMR" and method == "CPU":
            fname = "xmrcpuwin.zip"

        elif coin == "XMR" and method == "AMD":
            fname = "xmramdwin.zip"

        elif coin == "XMR" and method == "NVIDIA":
            fname = "xmrnvwin.zip"

        elif coin == "ZEC" and method == "CPU":
            fname = "zeccpuwin.zip"

        elif coin == "ZEC" and method == "AMD":
            fname = "zecamdwin.zip"

        elif coin == "ZEC" and method == "NV":
            fname = "zecnvwin.zip"

        elif coin == "ETH":
            fname = "ethwin.zip"
        print(coin)
    elif os() == "Darwin":
        pass

    elif os() == "Linux":
        pass

    else:
        print("OS not supported")
    
    urllib.request.urlretrieve(url+fname, fname)
    return fname