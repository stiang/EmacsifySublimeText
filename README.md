# Emacsify Sublime Text 2

## What is it?

This is a collection of commands and key bindings to make [Sublime Text 2][1] as
Emacs-like as possible, without sacrificing any of the native ST2 niceties.

### Features

* Uses the native marks and kill ring introduced in Alpha Build 2027
* Settings a mark and moving the cursor with the regular Emacs cursor moving shortcuts (C-n, C-b, C-a etc.) will create a visible selection
* Yanking will clear the selection
* C-g will cancel any marks/selections and close any open panels
* C-o works as expected
* C-x, C-s will save the buffer
* C-x, b will open the Goto File overlay

## Usage

At least on OS X I was not able to simply double-click a package file to install
it, so I had to do the following: 

* Quit ST2
* Copy EmacsifySublimeText.sublime-package to your DATADIR/Installed Packages folder
* Restart ST2. 

You may have to create the "Installed Packages" folder manually first.

## Known issues

* Setting a mark, then moving the cursor in a non-Emacs way, will not update the selection. This may cause unexpected behavior. Use C-g to reset things.
* Tapping C-a once will go to the start of the line, tapping it a second time will go to the first text on that line. This is feature, not a bug, but it is slightly different than what a standard Emacs would do
* There is no way to select which entry in the kill ring to yank, it will always yank the last one

Also, there is a small gotcha in the key bindings: I have set up C-w to select 
the current word, like in TextMate, then to extend to the next (soft) word part, but 
that doesn’t fit well with the default Emacs key bindings, where C-w means 
kill-region. So C-w is bound to an ExtendOrKill command, which switches between 
these two behaviors, based on whether a mark has been set. If a mark has been set, 
do kill-region. If not, expand the selection. For me, this works quite well, but it’s
something you should be aware of.

## Contribute
The source files for the package is in the "package-source" directory. Please fork and add pull requests 
if you would like to improve this package.

## Author
Stian Grytøyr (stian at grytoyr dot net)

[1]: http://www.sublimetext.com/2