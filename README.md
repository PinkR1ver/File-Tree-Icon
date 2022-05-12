# File Icon Tree

This repository is meant to gengerate beautiful and clear file tree to make your project file structure more clearly, fast and simply.

## User instruction

Now, this tool only have the basic function.
```
python itree.py [root]
```

Then you can get the file structure in your root dir.

Example of this repository:
```
📦 .
┣ 📂 .git
┃ ┣ 📂 hooks
┃ ┃ ┣ 📄 applypatch-msg.sample
┃ ┃ ┣ 📄 commit-msg.sample
┃ ┃ ┣ 📄 fsmonitor-watchman.sample
┃ ┃ ┣ 📄 post-update.sample
┃ ┃ ┣ 📄 pre-applypatch.sample
┃ ┃ ┣ 📄 pre-commit.sample
┃ ┃ ┣ 📄 pre-merge-commit.sample
┃ ┃ ┣ 📄 pre-push.sample
┃ ┃ ┣ 📄 pre-rebase.sample
┃ ┃ ┣ 📄 pre-receive.sample
┃ ┃ ┣ 📄 prepare-commit-msg.sample
┃ ┃ ┣ 📄 push-to-checkout.sample
┃ ┃ ┗ 📄 update.sample
┃ ┣ 📂 info
┃ ┃ ┗ 📄 exclude
┃ ┣ 📂 objects
┃ ┃ ┣ 📂 info
┃ ┃ ┗ 📂 pack
┃ ┣ 📂 refs
┃ ┃ ┣ 📂 heads
┃ ┃ ┗ 📂 tags
┃ ┣ 📄 config
┃ ┣ 📄 description
┃ ┗ 📄 HEAD
┣ 📂 output
┃ ┗ 📄 itree.exe
┣ 📄 itree.py
┗ 📄 README.md
```

## Bin

Using *pyinstaller* get **exe** file in dir `bin`. 