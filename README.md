# File Icon Tree

This repository is meant to gengerate beautiful and clear file tree to make your project file structure more clearly, fast and simply.

## User instruction

Using this:
```
python itree.py [argv] [root]
```

Then you can get the file structure in your root dir.

Now argv have this:
* **-v, --version**: show version
* **-h**: show hidden files
* **--help**: show help
* **-d, --depth [number]**:  set the depth we will show, default is 5

Example of this repository `python .\itree.py -d 2 -h .`
```
📦 .
┣ 📂 .git
┃ ┣ 📂 hooks
┃ ┣ 📂 info
┃ ┣ 📂 logs
┃ ┣ 📂 objects
┃ ┣ 📂 refs
┃ ┣ 📄 COMMIT_EDITMSG
┃ ┣ 📄 config
┃ ┣ 📄 description
┃ ┣ 📄 FETCH_HEAD
┃ ┣ 📄 HEAD
┃ ┣ 📄 index
┃ ┗ 📄 ORIG_HEAD
┣ 📂 bin
┃ ┗ 📄 itree.exe
┣ 📄 itree.py
┣ 📄 LICENSE
┗ 📄 README.md
```

## Bin

Using *pyinstaller* get **exe** file in dir `bin`. 