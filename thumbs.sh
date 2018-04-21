#!/bin/bash
# generate thumbnails, execute in jekyll _rootdir_
IMG_PATH=images/2018-1-15-mpc-service
IMG_TYPE=jpg
CONV_OPTS="-resize 222"

function GetBaseName() {
  FILENAME=$(basename $1)
  echo ${FILENAME%.*}
}

function GetExtension() {
  FILENAME=$(basename $1)
  echo "${FILENAME##*.}"
}

if [ "$1" = "doit" ]; then
  for i in $IMG_PATH/*$IMG_TYPE; do
    BASE=$(GetBaseName $i)
    EXT=$(GetExtension $i)
    THUMB="$IMG_PATH/$BASE-th.$EXT"
    convert $i $CONV_OPTS $THUMB
  done
else
  for i in $IMG_PATH/*$IMG_TYPE; do
    BASE=$(GetBaseName $i)
    EXT=$(GetExtension $i)
    THUMB="$IMG_PATH/$BASE-th.$EXT"
    #echo file base: $BASE;
    #echo file ext: $EXT
    #echo thumbnail: $THUMB
    echo convert $i $CONV_OPTS $THUMB
    echo ""
  done
fi


