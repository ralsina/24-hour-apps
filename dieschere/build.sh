#!/bin/sh
pyrcc4 icons.qrc -o icons_rc.py
pyuic4 main.ui -o Ui_main.py -x
