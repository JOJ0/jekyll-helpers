#!/bin/bash
# generate thumbnails, execute in jekyll _rootdir_
IMG_PATH="$1"
IMG_TYPE=hardcoded
NAME_SUFFIX="-th"

CONV_OPTS="-resize 333"    # use for thumbnails
#CONV_OPTS="-resize 1280"    # max size for full-width pics

# disable case sensitive globbing
shopt -s nocaseglob

if [[ -z $1 ]]; then
    echo "Usage: ./thumbs.sh <path> [doit]"
    exit 1
fi

function GetBaseName() {
  FILENAME=$(basename $1)
  echo ${FILENAME%.*}
}

function GetExtension() {
  FILENAME=$(basename $1)
  echo "${FILENAME##*.}"
}

if [ "$2" = "doit" ]; then
  for i in $IMG_PATH/*jpg; do
    BASE=$(GetBaseName $i)
    EXT=$(GetExtension $i)
    THUMB="$IMG_PATH/$BASE$NAME_SUFFIX.$EXT"
    convert $i $CONV_OPTS $THUMB
  done
  for i in $IMG_PATH/*png; do
    BASE=$(GetBaseName $i)
    EXT=$(GetExtension $i)
    THUMB="$IMG_PATH/$BASE$NAME_SUFFIX.$EXT"
    convert $i $CONV_OPTS $THUMB
  done
else
  for i in $IMG_PATH/*jpg; do
    BASE=$(GetBaseName $i)
    EXT=$(GetExtension $i)
    THUMB="$IMG_PATH/$BASE$NAME_SUFFIX.$EXT"
    #echo file base: $BASE;
    #echo file ext: $EXT
    #echo thumbnail: $THUMB
    echo convert $i $CONV_OPTS $THUMB
    echo ""
  done
  for i in $IMG_PATH/*png; do
    BASE=$(GetBaseName $i)
    EXT=$(GetExtension $i)
    THUMB="$IMG_PATH/$BASE$NAME_SUFFIX.$EXT"
    #echo file base: $BASE;
    #echo file ext: $EXT
    #echo thumbnail: $THUMB
    echo convert $i $CONV_OPTS $THUMB
    echo ""
  done
fi
# reactivate normal globbing
shopt -u nocaseglob
