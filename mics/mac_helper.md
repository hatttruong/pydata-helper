# Mapping keyboard between Mac & Windows #

## Terminal

[Reference](https://www.topbug.net/blog/2013/04/14/install-and-use-gnu-command-line-tools-in-mac-os-x/)

### HomeBrew

```
# install HomeBrew
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ export PATH="$(brew --prefix coreutils)/libexec/gnubin:/usr/local/bin:$PATH"
```

### Install the GNU Command Line Tools

```
$ brew install coreutils
$ brew install make
$ brew install wget
$ brew install screen
$ brew install git
$ brew install openssh
$ brew install unzip
# Homebrew installs pip pointing to the Homebrew’d Python 3 for you.
$ brew install python 

```