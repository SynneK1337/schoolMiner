from subprocess import check_output
from os import name


def get_architecture():
    if name == "nt":
        if check_output('wmic OS get OSArchitecture').decode('utf-8').replace('OSArchitecture', '').split()[0] == "32-bit" or check_output('wmic OS get OSArchitecture').decode('utf-8').replace('OSArchitecture', '').split()[0] == "32-bitowy":
            return 32
        else:
            return 64

    else:
        if check_output(['uname', "-m"]).decode('utf-8') == "x86":
            return 32
        else:
            return 64
