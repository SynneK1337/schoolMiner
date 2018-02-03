from os import chdir, getlogin
from platform import system as os
import ftplib

ftp = ftplib.FTP("localhost")
ftp.login("synnek", "jp2gmd")
ftp.cwd("/")


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
    
    with open(filename, "wb") as target:
        print("Downloading...")
        ftp.retrbinary("RETR " + filename, target.write)
        print("Downloaded")
    return filename
    ftp.close()
