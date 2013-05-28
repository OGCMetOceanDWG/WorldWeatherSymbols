#!/bin/sh

# WWS command suite
#
## generate PNG images
## pretty print SVG files

if [ $# -ne 1 ]; then
  cat <<END
Usage: `basename $0` <png>
  png: generate PNG versions of symbols

END
  exit 1
fi

COUNTER=0
THISDIR=`dirname $0`
ROOTDIR=$THISDIR/..
PNG_DIR=$ROOTDIR/png
TMP_DIR=$ROOTDIR/tmp
SVG_FILES=`find $ROOTDIR -type f -name "*.svg"`

case $1 in
    "png" )
    echo "Generating PNG images"
    if [ ! `which inkscape` >/dev/null ]; then
        echo "inkscape is not installed on this system.  Install with \`sudo apt-get install inkscape\`"
        exit 2
    fi    
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
    ;;
esac
