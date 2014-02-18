#!/bin/sh

for i in *.fig
do
  fig2dev -L eps "$i" "`basename $i .fig`.eps"
done
