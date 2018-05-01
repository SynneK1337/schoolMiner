from os import chdir, getlogin
from platform import system as os
import urllib.request

url = "http://synnek1337.github.io/miners/"


def download(coin, method):
    if os() == "Windows":
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
    elif os() == "Darwin":
        pass

    elif os() == "Linux":
        pass

    else:
        print("OS not supported")

    urllib.request.urlretrieve(url+fname, fname)
    return fname
