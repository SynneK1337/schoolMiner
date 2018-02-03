import zipfile

def unzip(file):
    with zipfile.ZipFile(file, 'r') as zip:
        zip.extractall("miner")
        print("miner unzipped")