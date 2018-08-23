# Some common actions in Git #


## Table of contents

* [Adding an existing project to GitHub using the command line](#adding-an-existing-project-to-github-using-the-command-line)
* [Set up username and password](#set-up-username-and-password)
* [Set up SSH](#set-up-ssh)

## Adding an existing project to GitHub using the command line

Links: https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/

- Create a new repository on GitHub. To avoid errors, do not initialize the new repository with README, license, or `gitignore` files. You can add these files after your project has been pushed to GitHub.
- Open Git Bash.
- Change the current working directory to your local project.
- Initialize the local directory as a Git repository.
```
$ git init
```
- Add the files in your new local repository. This stages them for the first commit.
```
$ git add .
# Adds the files in the local repository and stages them for commit. To unstage a file, use ' git rm --cached YOUR-FILE'.
```
- Commit the files that you've staged in your local repository.
```
$ git commit -m "First commit"
```
- At the top of your GitHub repository's Quick Setup page, click  to copy the remote repository URL.
- In the Command prompt, add the URL for the remote repository where your local repository will be pushed.
```
$ git remote add origin https://github.com/abc/xyz.git
# Sets the new remote
$ git remote -v
# Verifies the new remote URL
```
- Push the changes in your local repository to GitHub.
```
$ git push origin master
# Pushes the changes in your local repository up to the remote repository you specified as the origin
```

## Set up username and password

```
# install git (MAC)
$ git --version
# If you don’t have it installed already, it will prompt you to install it.

$ git config --global user.name "Ha Truong"
$ git config --global user.email "xxx@gmail.com"
```

## Set up SSH

1. [Generating a new SSH key and adding it to the ssh-agent](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)
2. [Adding a new SSH key to your GitHub account](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)

```
# generate new SSH Key
$ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
Generating public/private rsa key pair.
$ Enter a file in which to save the key (/c/Users/you/.ssh/id_rsa):[Press enter]
$ Enter passphrase (empty for no passphrase): [Type a passphrase]
$ Enter same passphrase again: [Type passphrase again]

# Adding your SSH key to the ssh-agent
# start the ssh-agent in the background
$ eval $(ssh-agent -s)
Agent pid 59566
# If you're using macOS Sierra 10.12.2 or later, you will need to modify your ~/.ssh/config file to automatically load keys into the ssh-agent and store passphrases in your keychain.

Host *
 AddKeysToAgent yes
 IgnoreUnknown UseKeychain
 UseKeychain yes
 IdentityFile ~/.ssh/id_rsa

$ ssh-add -K ~/.ssh/id_rsa

$ pbcopy < ~/.ssh/id_rsa.pub
# Copies the contents of the id_rsa.pub file to your clipboard

# In the upper-right corner of any page, click your profile photo, then click Settings.
# In the user settings sidebar, click SSH and GPG keys.
# Click New SSH key or Add SSH key...
```
