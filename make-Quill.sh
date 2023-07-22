#!/bin/sh

./lisp.sh --dynamic-space-size $((32*1024*1024))			\
          --load Quill.lisp						                \
	  --eval '(in-package :quill)'					            \
	  --eval "(sb-ext:save-lisp-and-die
     	            \"Quill\"
                  :executable t)"					            \
	  --eval '(print :Quill)'					                  \
	  --eval '(sb-ext:quit)'
