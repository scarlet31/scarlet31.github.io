#!/bin/sh

sbcl "$@"

exit 0

There is a lot to this file, although there are only 3 lines.

The first is the 'shebang' line.  It says to run this program thought /bin/sh, aka 'shell script'.

The sceone 'renames' sbcl, Steel Bank Common Lisp, to lisp.sh.  

This is so your lisp contains the options for --eval and --load.  

They are, or should be standard in all lisps.  

So you are given  the option of going higher level and programming a 'wrapper'.

That is what this is.  A 'wrapper' script.

The last line is to return that there was no errors.  
