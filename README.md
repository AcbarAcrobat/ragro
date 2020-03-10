# ragro


Preparatory Activities:
```
$ sudo apt install python3.8
$ sudo apt install python3-pip
```

Download and Install Allure on *Unix system
```
$ wget -i https://launchpad.net/~qameta/+archive/ubuntu/allure/+files/allure_2.4.1~xenial_all.deb
$ sudo dpkg -i allure_2.4.1~xenial_all.deb
$ sudo apt-get install -f
```

After that go to /path_to/ragro and create virtualenv
```
$ sudo python3 -m venv venv
$ source venv/bin/activate
```
Then install required packages with pip
```
$ pip install -r requirements.txt
```
And run the tests
```
$ pytest --reruns 3 --reruns-delay 1 -sv --alluredir=allure_results tests/
```

Looks your report
```
$ allure serve allure_results/
```
