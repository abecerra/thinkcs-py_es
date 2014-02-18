#!/bin/bash

for i in *.tex ; do  ./transform.py < "$i" > `basename "$i" .tex`.lore ; done
