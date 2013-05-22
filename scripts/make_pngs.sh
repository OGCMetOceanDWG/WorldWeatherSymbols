#!/bin/sh

# generate PNG images

COUNTER=0
THISDIR=`dirname $0`
ROOTDIR=$THISDIR/..
PNG_DIR=$ROOTDIR/png
SVG_FILES=`find $ROOTDIR -type f -name "*.svg"`

if [ ! -d "$PNG_DIR" ]; then
    mkdir $PNG_DIR
fi

for svg in $SVG_FILES
do
  BASENAME=`basename $svg .svg`
  convert $svg $PNG_DIR/$BASENAME.png
  COUNTER=$((COUNTER+$?))
done

exit $COUNTER

