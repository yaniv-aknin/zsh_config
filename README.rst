Introduction
============

Installation
============
Just copy .zshrc and .zsh.d to your home directory.

NOTE TO MAC USERS
-----------------
If you want Ctrl+Backspace to work properly (triggering backward-kill-word), you will have to make your terminal send the proper sequence (the default is triggered by \e?, so for instance in iTerm you would make Ctrl-backspace send escape sequence '?').

Features
========

General Shell Stuff
-------------------

* Directory cycling: Ctrl+Shift-Left/Right cycles directories in the dirstack left or right
* Ctrl+Shift+Up triggers 'cd ..'
* Ctrl+P issues *popd*.


Python
------

* *virtualenvwrapper* integration -- shell starts in __global__ virtualenv by default.
* cdpy: utility to *cd* into the directory holding the given package
* mkpkg: shortcut for mkdir + touch __init__.py file
