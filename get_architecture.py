from subprocess import check_output
from os import name

def get_architecture():
    if name == "nt":
        if check_output('wmic OS get OSArchitecture').decode('utf-8').replace('OSArchitecture', '').split()[0] == "64-bit":
            return 64
        else:
            return 32

    else:
        if check_output(['uname', "-m"]).decode('utf-8') == "x86_64":
            return 64
        else:
            return 32
