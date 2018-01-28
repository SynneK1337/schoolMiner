from eth import gpu_filename as eth_gpu_filename
from os import chdir, getlogin
from platform import system
import ftplib

ftp = ftplib.FTP("localhost")
ftp.login("synnek", "jp2gmd")

def eth_gpu():
    if system() == "Windows":
        chdir(r'C:\Users\%s' % (getlogin()))

    ftp.cwd('/')
    ftp.retrbinary("RETR " + eth_gpu_filename, open(eth_gpu_filename, 'wb').write)
    ftp.quit()