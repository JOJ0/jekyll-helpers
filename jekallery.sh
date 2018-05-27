#!/bin/bash
# generate markdown files for jekyll collection,
# execute from jekyll _rootdir_
COLL_PATH=_das-adhs-7-seg
IMG_PATH=images/2017-9-24-das-adhs-7-seg
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
  mkdir -p $COLL_PATH
  for i in $IMG_PATH/*$IMG_TYPE; do
    if [[ $i != *"-th".$IMG_TYPE* ]]; then
      MD_FILE=$COLL_PATH/$(GetMarkdownName $i)
      PrintMarkdown $i > $MD_FILE
    fi
  done
else
  for i in $IMG_PATH/*$IMG_TYPE; do
    if [[ $i != *"-th".$IMG_TYPE* ]]; then
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
    fi
  done
fi


