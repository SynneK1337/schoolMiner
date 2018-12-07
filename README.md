# schoolMiner
Useful utility that helps you starting up cryptocurrency miner. Useful to run a miner by single click in your school, public library or sth.

## Used miners
* Claymore CryptoNote CPU Miner **(Monero, Electroneum)**
* More comming soon

## Usage
**IF POSSIBLE, RUN THIS SCRIPT AS ADMIN**
### Using prepared config
First of all, edit your ```config.cfg``` file, enter your address and pool. Then execute
```python schoolminer.py -c``` or ```python schoolminer.py --use-config```

### Using **TUI**
```python schoolminer.py```
Then enter your address and pool

### Pre-compiled binary to use without python installed
Pre-compiled .exe binary is available to donwload in **Releases** tab
Usage is almost the same, you can either use TUI or prepared-config method.

## Credits
* [joeware](http://www.joeware.net) for creating quiet.exe
* Claymore for creating miners