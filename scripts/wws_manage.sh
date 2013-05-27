#!/bin/sh

# WWS command suite
#
## generate PNG images
## pretty print SVG files

if [ $# -ne 1 ]; then
  cat <<END
Usage: `basename $0` <png|pp>
  png: generate PNG versions of symbols
  pp: pretty print SVG files

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
    "pp" )
    echo "Pretty printing SVG files"
    if [ ! `which svgpp` >/dev/null ]; then
        echo "svgpp is not installed on this system.  Install with \`sudo apt-get install libbatik-java\`"
        exit 2
    fi
    if [ ! -d "$TMP_DIR" ]; then
        mkdir $TMP_DIR
    fi

    for svg in $SVG_FILES
    do
      BASENAME=`basename $svg .svg`
      svgpp $svg $TMP_DIR/$BASENAME.svg
      status=$?
      if [ $status -ne 0 ]; then
          COUNTER=$((COUNTER+1))
      else
          mv -f $TMP_DIR/$BASENAME.svg $svg
      fi
    done
    rmdir $TMP_DIR
    ;;
esac
