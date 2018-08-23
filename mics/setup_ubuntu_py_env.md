# Ubuntu Command #

## Table of contents

* [Commands related to OS](#commands-related-to-os)
    - [Typical commands](#typical-commands)
    - [Connect via SSH](#connect-via-ssh)
    - [Screen command](#screen-command)
    - [Files, Directory](#files-directory)
    - [Disk](#disk)
    - [Permission](#permissions)
* [Setup Disk Storage in Linux](#setup-disk-storage-in-linux)
* [Create auto connect to server with shell script using expect](#create-auto-connect-to-server-with-shell-script-using-expect)
* [Set up environment for Python](#set-up-environment-for-python)

## Commands related to OS

### Typical commands

```
# Reboot
$ sudo reboot
```

### Connect via SSH:

```
# SSH
$ ssh <user_name>@<ip_address>
```

### Screen command

```
# list all screens
$ screen -l

# attach screen
$ screen -r <screen_number>

# deattach screen: Ctrl-A+D
# terminate screen: Ctrl-D
```

### Files, Directory

```
# list all files in directory: 
# -l: detail
# -t: order by last modified date, -tr: reverse
# --block-size=M

$ sudo ls YOUR_DIR -l

# COUNT_FILES in directory
$ sudo find YOUR_DIR -type f | wc -l

# calculate SIZE_OF_FOLDER
$ sudo du -sh file_path

# ZIP all files of folder
$ zip -r myfiles.zip mydir

# count number of lines START_WITH_SOMETHING in a specific file
$ awk '/^yourcheckstring/{a++}END{print a}' file_path
```

### Disk

```
# check disk
$ df -h

# check remaining of current directory
$ du -sh
```

### Permissions

```
# Give execute permission to your script
$ chmod +x /path/to/yourscript.sh
```

## Setup Disk Storage in Linux

**Situtaion**:

**Solution**: [Setup Flexible Disk Storage with Logical Volume Management (LVM) in Linux](https://www.tecmint.com/create-lvm-storage-in-linux/)


## Create auto connect to server with shell script using expect
In some cases, you need to connect to server or copy from/to server which is protected by password and these actions usually happens. It's completely boring to enter not-easy-to-remember password over the time. Hence, to create a bat script to make this process automatic is necessary.

* install expect package
```
sudo apt-get install tcl8.5
sudo apt-get install expect
```

* create connect shell script
```
#!/usr/bin/expect -f
spawn ssh -o GSSAPIAuthentication=no [your_user_name]@x.x.x.x
expect "password:"
send "[your_password]\r"
interact
```

Then, simply run `./connect.sh`

* create copy shell script (copy from local to server)
```
#!/usr/bin/expect -f
set src_file [lindex $argv 0]
set dest_file [lindex $argv 1]
spawn scp -r $src_file [your_username]@[your_id_address]:$dest_file
expect "password:"
send "[your_password]\r"
interact
```

* create copy shell script (copy from server to local)
```
#!/usr/bin/expect -f
set src_file [lindex $argv 0]
set dest_file [lindex $argv 1]
spawn scp -r [your_username]@[your_id_address]:$src_file $dest_file
expect "password:"
send "[your_password]\r"
interact
```

Note: "-r" means copy the entire folder

## Set up environment for Python

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