#!/bin/bash
# generate markdown files for jekyll collection,
# execute from jekyll _rootdir_
COLL_PATH=_mpc-service
IMG_PATH=images/2018-1-15-mpc-service
IMG_TYPE=jpg

#set -x

function GetBaseName() {
  FILENAME=$(basename $1)
  echo ${FILENAME%.*}
}

function GetMarkdownName() {
  FILENAME=$(basename $1)
  echo "${FILENAME%.*}.md"
}

function GetExtension() {
  FILENAME=$(basename $1)
  echo "${FILENAME##*.}"
}

function PrintMarkdown() {
    echo "---"
    BASE=$(GetBaseName $1)
    echo "title: $BASE"
    echo "image-path: /$1"
    echo "caption: \"\""
    echo "---";
}

if [ "$1" = "doit" ]; then
  for i in $IMG_PATH/*$IMG_TYPE; do
    MD_FILE=$COLL_PATH/$(GetMarkdownName $i)
    PrintMarkdown $i > $MD_FILE
  done
else
  for i in $IMG_PATH/*$IMG_TYPE; do
    BASE=$(GetBaseName "$i")
    EXT=$(GetExtension "$i")
    MD_FILE=$COLL_PATH/$(GetMarkdownName $i)
    THUMB=$IMG_PATH/$BASE-th.$EXT
    #echo file base: $BASE
    echo file ext: $EXT
    echo markdown name: $MD_FILE
    #echo thumbnail: $THUMB
    echo markdown contents:
    PrintMarkdown $i
    echo ""
  done
fi


