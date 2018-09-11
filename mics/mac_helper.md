# MACOS Commands #

## Table of contents

* [Install HomeBrew](#homebrew)
* [Install the GNU Command Line Tools](#install-the-gnu-command-line-tools)
* [Common Cmd](#common-cmd)
* [Files/Directory](#filesdirectory)
* [Zip/Unzip](#zipunzip)
* [Permissions](#permissions)
* [Python environment](#set-up-environment-for-python)
* [Setup Java](#set-up-java)
* [Setup VNP](#set-up-vpn)
* []()

## Terminal

[Reference](https://www.topbug.net/blog/2013/04/14/install-and-use-gnu-command-line-tools-in-mac-os-x/)

## HomeBrew

```
# install HomeBrew
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ export PATH="$(brew --prefix coreutils)/libexec/gnubin:/usr/local/bin:$PATH"
```

## Install the GNU Command Line Tools

```
$ brew install coreutils
$ brew install make
$ brew install wget
$ brew install screen
$ brew install git
$ brew install openssh
$ brew install unzip
$ brew install htop
# Homebrew installs pip pointing to the Homebrew’d Python 3 for you.
$ brew install python

```

## Common Cmd

```
# wget in MacOS
$ curl <your_url> -o <filename>

# Ctrl-F5
$ cmd + Shift + R
```

## Files/Directory

* **FILES**

```
# count number of files in directory
$ ls your_directory | wc -l

# list files with size
$ ls -lh  your_path

# delete files with certain extension
$ find /path -name '*.csv' -delete
```

* **FOLDERS**

```
# list folders with size
$ du -sh /path/to/dir/*

# remove directory
$ rmdir <your_dir>

```

## Zip/Unzip

```
$ zip -r <name_of_zipped_file> <name_of_folder_to_be_zipped>
$ unzip <name_of_zipped_file>

# tar.xz
$ tar -cJf filename.tar.xz /path/to/folder_or_file ...
$ tar xf filename.tar.xz
```

## Permissions

```
$ chmod +x script.sh
```

## Set up environment for Python

```
$ brew install python3
# Then, the pip or pip3 is installed automatically, and you can install any package by `pip install <package>`

# install jupyter notebook
$ pip3 install --upgrade pip
$ pip3 install jupyter

# install some important package
$ pip3 install scikit-learn
$ pip3 install gensim
$ pip3 install nltk
$ pip3 install pandas

```

## Set up JAVA

```
# install
$ brew cask install java
# verify
$ brew cask info java
```

## Set up VPN
* Install [Tunnelblick](https://tunnelblick.net/)
*