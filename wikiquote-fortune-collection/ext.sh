#!/bin/sh

for f in *.cpp; do

#This line splits the file name on the delimiter "."
baseName=`echo $f | cut -d "." -f 1`
newExtension=""

cp $f $baseName$newExtension

done
