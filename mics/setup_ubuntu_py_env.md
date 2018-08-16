# Ubuntu Command #

## 1. Commands related to OS

### 1. Typical command:

```
# SSH
$ ssh <user_name>@<ip_address>

# Reboot
$ sudo reboot

# Screen

# list all screens
$ screen -l

# attach screen
$ screen -r <screen_number>

# deattach screen: Ctrl-A+D
# terminate screen: Ctrl-D
```

### 2. Setup Disk Storage in Linux

**Situtaion**:

**Solution**: [Setup Flexible Disk Storage with Logical Volume Management (LVM) in Linux](https://www.tecmint.com/create-lvm-storage-in-linux/)


## 2. Set up environment for Python
    ```
    # install pip
    $ sudo apt-get update
    $ sudo apt-get install python-pip

    # OR
    $ sudo apt install python2.7 python-pip
    $ sudo pip2 install <package>

    # install pip3
    $ sudo apt-get update
    $ sudo apt-get install python3-pip

    # install jupyter notebook
    $ sudo apt-get -y install ipython ipython-notebook
    $ sudo -H pip3 install jupyter

    # install some important package
    $ sudo pip3 install scikit-learn
    $ sudo pip3 install gensim
    $ sudo pip3 install nltk
    $ sudo pip3 install pandas

    # install screen
    $ sudo apt-get update
    $ sudo apt-get install screen

    # install htop
    $ sudo apt install htop
    
    ```