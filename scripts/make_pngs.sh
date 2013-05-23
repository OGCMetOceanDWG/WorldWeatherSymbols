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
  inkscape -f $svg -e $PNG_DIR/$BASENAME.png --g-fatal-warnings -l
  status=$?
  if [ $status -ne 0 ]; then
      COUNTER=$((COUNTER+1))
  fi
done

exit $COUNTER
