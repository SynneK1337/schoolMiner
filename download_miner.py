from eth import gpu_filename as eth_gpu_filename
from xmr import nv_filename as xmr_nv_filename
from xmr import amd_filename as xmr_amd_filename
from xmr import cpu_filename as xmr_cpu_filename
from zec import cpu_filename as zec_cpu_filename
from zec import nv_filename as zec_nv_filename
from zec import amd_filename as zec_amd_filename
from os import chdir, getlogin
from platform import system
import ftplib

ftp = ftplib.FTP("localhost")
ftp.login("synnek", "jp2gmd")
ftp.cwd('/')


def eth_gpu():
    if system() == "Windows":
        chdir(r'C:\Users\%s' % (getlogin()))    
        ftp.retrbinary("RETR " + eth_gpu_filename, open(eth_gpu_filename, 'wb').write)
    
    elif system() == "Darwin":
        pass

    elif system() == "Linux":
        pass

    else:
        print("Unsupported OS.")

    ftp.quit()


def xmr_cpu():
    if system() == "Windows":
        chdir(r'C:\Users\%s' % (getlogin()))
        ftp.retrbinary("RETR " + xmr_cpu_filename, open(xmr_cpu_filename, 'wb').write)

    elif system() == "Darwin":
        pass

    elif system() == "Linux":
        pass

    else:
        print("Unsupported OS")

    ftp.quit()
def xmr_gpu(gpu):
    if system() == "Windows":
        chdir(r'C:\Users\%s' % (getlogin()))
        if gpu == "NVIDIA":
            ftp.retrbinary("RETR " + xmr_nv_filename, open(xmr_nv_filename, 'wb').write)
        elif gpu == "AMD":
            ftp.retrbinary("RETR " + xmr_amd_filename, open(xmr_amd_filename, 'wb').write)
    elif system() == "Darwin":
        pass

    elif system() == "Linux":
        pass

    else:
        print("Unsupported OS")

    ftp.quit()

def zec_cpu():
    if system() == "Windows":
        chdir(r'C:\Users\%s' % (getlogin()))
        ftp.retrbinary("RETR " + zec_cpu_filename, open(zec_cpu_filename, 'wb').write)

    elif system() == "Darwin":
        pass
    
    elif system() == "Linux":
        pass

    else:
        print("Unsupported OS")

    ftp.quit()

def zec_gpu(gpu):
    if system() == "Windows":
        chdir(r'C:\Users\%s' % (getlogin()))
        if gpu == "AMD":
            ftp.retrbinary("RETR " + zec_gpu_filename, open(zec_amd_filename, 'wb').write)
        elif gpu == "NVIDIA":
            ftp.retrbinary("RETR " + zec_nv_filename, open(zec_nv_filename, 'wb').write)
    elif system() == "Darwin":
        pass
    
    elif system() == "Linux":
        pass

    else:
        print("Unsupported OS")

    ftp.quit()