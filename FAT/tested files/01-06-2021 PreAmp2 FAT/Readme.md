# Lastronics Laser Amplifier
## 1. Run prequisite python packages
[pip](https://pip.pypa.io/en/stable/)
```bash
sudo apt-get install python3 python3-pip 
pip3 install -r requirements.txt
```
## 2. Edit [config.py](./config.py) to configure device information and test parameters
## 3. Run pytest using following command (prefix with 'python -m' when running from windows cmd)
[Pytest](https://docs.pytest.org/en/stable/)
```bash
pytest [destination of file] -s --html=Report.html --self-contained-html --verbose --capture sys -rP -rF
```


