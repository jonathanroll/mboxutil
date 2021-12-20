#!/bin/zsh

for ((n=9; n<13; n++)); do ln -s Inbox\ $n.mbox/mbox ./mbox$n ; done
