from os import chdir, getlogin
from platform import system as os
import urllib.request

url = "http://127.0.0.1/" #Enter your HTTP Server here, soon


def download(coin, method):
    if os() == "Windows":
        print("OS is Windows")
        chdir(r'C:\Users\%s' % getlogin())
        if coin == "XMR" and method == "CPU":
            filename = "xmrcpuwin.zip"

        elif coin == "XMR" and method == "AMD":
            filename = "xmramdwin.zip"

        elif coin == "XMR" and method == "NVIDIA":
            filename = "xmrnvwin.zip"

        elif coin == "ZEC" and method == "CPU":
            filename = "zeccpuwin.zip"

        elif coin == "ZEC" and method == "AMD":
            filename = "zecamdwin.zip"

        elif coin == "ZEC" and method == "NV":
            filename = "zecnvwin.zip"

        elif coin == "ETH":
            filename = "ethwin.zip"

    elif os() == "Darwin":
        pass

    elif os() == "Linux":
        pass

    else:
        print("OS not supported")
    
    urllib.request.urlretrieve(url+filename, filename)
    return filename